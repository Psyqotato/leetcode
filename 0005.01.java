class Solution {
    public String longestPalindrome(String s) {
        if (s == "" || s.length() == 1) {
            return s;
        }
        String result = s.substring(0, 1);
        for (int i = 1; i < s.length(); i++) {
            int mid = (result.length() - 1) / 2;
            int left;
            int right;
            String subre;
            if (i - mid > 0 && i + mid <= s.length() - 1) {
                subre = new StringBuffer(s.substring(i, i + mid + 1)).reverse().toString();
                if (s.charAt(i) == s.charAt(i - 1) && subre.equals(s.substring(i - mid - 1, i))) {
                    left = i - mid - 1;
                    right = i + mid;
                    while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
                        left = left - 1;
                        right = right + 1;
                        if (right - left > result.length()) {
                            result = s.substring(left + 1, right);
                        }
                    }
                }
                subre = new StringBuffer(s.substring(i + 1, i + mid + 1)).reverse().toString();
                if (subre.equals(s.substring(i - mid, i))) {
                    left = i - mid;
                    right = i + mid;
                    while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
                        left = left - 1;
                        right = right + 1;
                        if (right - left > result.length()) {
                            result = s.substring(left + 1, right);
                        }
                    }
                }
            }
        }
        return result;
    }
}