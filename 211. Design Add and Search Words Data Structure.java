/*Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.*/

class WordDictionary {
    // The children map stores characters as keys and WordDictionary instances as
    // values.
    HashMap<Character, WordDictionary> children;
    // This boolean flag indicates whether the current node represents the end of a
    // word.
    boolean isWord;

    // Constructor to initialize the WordDictionary.
    public WordDictionary() {
        this.children = new HashMap<>();
        this.isWord = false;
    }

    // Method to add a word to the dictionary.
    public void addWord(String word) {
        if (word.length() == 0) {
            // If the word is empty, mark the current node as the end of a word.
            this.isWord = true;
            return;
        }
        char firstChar = word.charAt(0);
        if (!children.containsKey(firstChar)) {
            // If the character is not in the children map, create a new WordDictionary
            // node.
            children.put(firstChar, new WordDictionary());
        }
        // Recursively add the rest of the word to the children of the current node.
        children.get(firstChar).addWord(word.substring(1));
    }

    // Method to search for a word in the dictionary.
    public boolean search(String word) {
        return dfs(word);
    }

    // Helper method for searching, using depth-first search (dfs).
    private boolean dfs(String word) {
        if (word.length() == 0) {
            // If the word is empty, check if the current node represents the end of a word.
            return this.isWord;
        }
        char firstChar = word.charAt(0);

        if (firstChar == '.') {
            // If the first character is a '.', try matching the rest of the word with any
            // children.
            for (Map.Entry<Character, WordDictionary> entry : children.entrySet()) {
                WordDictionary wordDictionary = entry.getValue();
                if (wordDictionary.dfs(word.substring(1))) {
                    return true;
                }
            }
            return false;
        }

        if (!children.containsKey(firstChar)) {
            // If the character is not in the children map, the word is not in the
            // dictionary.
            return false;
        }
        // Recursively search for the rest of the word in the children of the current
        // node.
        return children.get(firstChar).search(word.substring(1));
    }
}
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */