'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
'''
class Solution {
    public boolean backspaceCompare(String S, String T) {
     if (S == null || T == null) return false;

          return type(S).equals(type(T));
      }

    private String type(String s) {
        Stack<Character> st = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '#') {
                if (!st.isEmpty()) st.pop();
            } else {
                st.push(c);
            }
        }
        StringBuffer strb = new StringBuffer();
        while (!stack.isEmpty()) {
            strb.append(st.pop());
        }
        return strb.toString();
    }
}
