class Solution {
   public boolean canConvertString(String s, String t, int k) {
        int[] count = new int[26];
        for (int i = 0; i < Math.min(s.length(), t.length()); ++i) {
            int diff = (t.charAt(i) - s.charAt(i) + 26) % 26;
            if (diff > 0 && diff + count[diff] * 26 > k) {
                return false;
            }
            ++count[diff];
        }
        return s.length() == t.length();
    }
}