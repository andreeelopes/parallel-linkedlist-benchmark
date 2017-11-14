package cp.benchmark.intset;

import java.util.concurrent.atomic.AtomicMarkableReference;

import cp.benchmark.intset.IntSetLinkedListOptimisticPerNodeLock.Node;

/**
 * @author Pascal Felber
 * @author Tiago Vale
 * @since 0.1
 */
public class IntSetLinkedListLockFree implements IntSet {

	public class Node {
		private final int value;
		public AtomicMarkableReference<Node> next;

		public Node(int value, Node next) {
			this.value = value;
			this.next = new AtomicMarkableReference<Node>(next, false);
		}

		public Node(int value) {
			this(value, null);
		}

		public int getValue() {
			return value;
		}
	}

	public class Window {
		public Node pred, curr;
		public Window(Node myPred, Node myCurr){
			pred = myPred; curr = myCurr;
		}
	}

	private final Node m_first;

	public IntSetLinkedListLockFree() {
		Node max = new Node(Integer.MAX_VALUE);
		Node min = new Node(Integer.MIN_VALUE, max);
		m_first = min;
	}

	public boolean add(int value) {
		while(true) {
			Window window = find(m_first, value);
			Node pred = window.pred, curr = window.curr; 
			if(curr.getValue() == value)
				return false;
			else {
				Node node = new Node(value, curr);
				if (pred.next.compareAndSet(curr, node, false, false))
					return true;
			}
		}
	}

	public boolean remove(int value) {
		boolean snip;
		while(true) {
			Window window = find(m_first, value);
			Node pred = window.pred, curr = window.curr;
			if (curr.getValue() != value)
				return false;
			else {
				Node succ = curr.next.getReference();
				snip = curr.next.compareAndSet(succ, succ, false, true);
				if(!snip)
					continue;
				pred.next.compareAndSet(curr, succ, false, false);
				return true;
			}
		}
	}

	public boolean contains(int value) {
		boolean[] marked = {false};
		Node curr = m_first; //head
		while(curr.getValue() < value) {
			curr = curr.next.getReference();
			curr.next.get(marked);
		}
		return (curr.getValue() == value && !marked[0]);
	}

	public void validate() {
		java.util.Set<Integer> checker = new java.util.HashSet<>();
		int previous_value = m_first.getValue();
		Node node = m_first.next.getReference();
		int value = node.getValue();
		while (value < Integer.MAX_VALUE) {
			assert previous_value < value : "list is unordered: " + previous_value + " before " + value;
			assert !checker.contains(value) : "list has duplicates: " + value;
			checker.add(value);
			previous_value = value;
			node = node.next.getReference();
			value = node.getValue();
		}
		//System.out.println("DEBUG: unmarked nodes = " + countUnmarkedNodes());
	}

	/**
	 * 
	 * @param head
	 * @param key
	 * @return a structure contains the nodes on either side of the key. It removes
	 * marked nodes when it encounters them.
	 */
	public Window find(Node head, int key) {
		Node pred = null, curr = null, succ = null;
		boolean[] marked = {false};
		boolean snip;
		retry: while(true) {
			pred = head;
			curr = pred.next.getReference();
			while(true) {
				succ = curr.next.get(marked);
				while(marked[0]) { //clean garbage
					snip = pred.next.compareAndSet(curr,  succ, false, false);
					if(!snip) continue retry;
					curr = succ;
					succ = curr.next.get(marked);
				}
				if(curr.getValue() >= key)
					return new Window(pred, curr);
				pred = curr;
				curr = succ;
			}
		}
	}

	private Node getUnmarkedNext(Node node) {
		boolean marked[] = {false};
		while (node.getValue() < Integer.MAX_VALUE) {
			node.next.get(marked);
			Node next = node.next.getReference();

			if(!marked[0])
				return next;
			node = next;
		}
		return node;
	}

	private int countUnmarkedNodes() {
		int counter = 0;
		Node node = m_first;
		boolean marked[] = {false};
		while (node.getValue() < Integer.MAX_VALUE) {
			node.next.get(marked);
			if(marked[0])
				counter++;
			node = node.next.getReference();
		}

		return counter;
	}
}
