public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> pre = null;
        for (int i = 1; i <= numRows; i++) {
            ArrayList<Integer> save = new ArrayList<>();
            for (int j = 1; j <= i; j++)
                if (j == 1 || j == i) save.add(1);
                else save.add(pre.get(j-1) + pre.get(j-2));
            result.add(save);
            pre = save;
        }
        return result;
    }
}