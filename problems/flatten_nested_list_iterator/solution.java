/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class NestedIterator implements Iterator<Integer> {

    /**
     * use to store the elements from given list
     */
    private List<Integer> elements = new ArrayList<>();

    /**
     * to keep track the element which need to show
     */
    int index = 0;

    public NestedIterator(List<NestedInteger> nestedList) {

        init(nestedList);
    }

    /**
     * store them recursively
     *
     * @param nestedList
     */
    private void init(List<NestedInteger> nestedList) {
        if (nestedList.isEmpty())
            return;

        for (NestedInteger nst : nestedList) {

            if (!nst.isInteger()) {
                init(nst.getList());

            } else
                elements.add(nst.getInteger());
        }
    }

    @Override
    public Integer next() {
        return elements.get(index++);

    }

    @Override
    public boolean hasNext() {
        if (index < this.elements.size())
            return true;
        else
            return false;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */