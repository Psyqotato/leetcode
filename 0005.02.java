class Solution {
    public String longestPalindrome(String s) {
        int slength = s.length();
        if (s == "" || slength == 1) {
            return s;
        }
        int leftend = 0, rightend = 1;
        for (int i = 1; i < slength; i++) {
            int mid = (rightend - leftend - 1) / 2;
            int left, right;
            String subre;
            if (i - mid > 0 && i + mid <= slength - 1) {
                subre = new StringBuffer(s.substring(i, i + mid + 1)).reverse().toString();
                if (s.charAt(i) == s.charAt(i - 1) && subre.equals(s.substring(i - mid - 1, i))) {
                    left = i - mid - 1;
                    right = i + mid;
                    while (left >= 0 && right <= slength - 1 && s.charAt(left) == s.charAt(right)) {
                        left = left - 1;
                        right = right + 1;
                        if (right - left > rightend - leftend) {
                            leftend = left + 1;
                            rightend = right;
                        }
                    }
                }
                subre = new StringBuffer(s.substring(i + 1, i + mid + 1)).reverse().toString();
                if (subre.equals(s.substring(i - mid, i))) {
                    left = i - mid;
                    right = i + mid;
                    while (left >= 0 && right <= slength - 1 && s.charAt(left) == s.charAt(right)) {
                        left = left - 1;
                        right = right + 1;
                        if (right - left > rightend - leftend) {
                            leftend = left + 1;
                            rightend = right;
                        }
                    }
                }
            }
        }
        return s.substring(leftend, rightend);
    }
}