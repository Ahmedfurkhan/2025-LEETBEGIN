class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merge = new StringBuilder();
        int i = 0, j=0;
        int len1 = word1.length();
        int len2 = word2.length();

        while (i < len1 || j < len2){
            if (i < len1){
                merge.append(word1.charAt(i));
                i++;
            }
            if (j < len2){
                merge.append(word2.charAt(j));
                j++;
            }
        }
        return merge.toString();
    }
}