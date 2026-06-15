class Solution {
    public int hammingWeight(int n) {
        
        int j = 0;
        int c = 0;
        String binary = Integer.toBinaryString(n);
        int i = binary.length() - 1;
        char[] arr = binary.toCharArray();

        while (j <= i) {
            if (arr[i] == '1' && i != j) {
                c++;
                
            }
            if (arr[j] == '1' && i != j) {
                c++;
                
            }
            if (i == j && arr[i] == '1') {
                c++;
                
            }

            i--;
            j++;
        }

        return c;
    }
}
