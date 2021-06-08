class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        ;
        int max_num = 1;
        List<Integer> nums = new ArrayList<>();
        for (int i = s.length(); i > 0; i--) {
            nums.add(i);
        }
        for (int i = 0; i < s.length(); i++) {
            if (nums.get(i) < max_num) {
                continue;
            }
            ;
            int left = i;
            int right = s.length() - 1;
            while (left < right && max_num < right - i + 1) {
                if (s.substring(left + 1, right + 1).indexOf(s.substring(left, left + 1)) != -1) {
                    right = s.substring(left + 1, right + 1).indexOf(s.substring(left, left + 1)) + left;
                    nums.set(left, right - left);
                }
                left = left + 1;
            }
            nums.set(i, right - i + 1);
            if (nums.get(i) > max_num) {
                max_num = nums.get(i);
            }
        }
        return max_num;
    }
}