

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> hashmap = new HashMap<>();

        hashmap.put(')', '(');
        hashmap.put(']', '[');
        hashmap.put('}', '{');

        for (char c : s.toCharArray()) {
            if (hashmap.containsKey(c)) { // closing bracket
                if (stack.isEmpty() || stack.pop() != hashmap.get(c)) {
                    return false;
                }
            } else { // opening bracket
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }

}
