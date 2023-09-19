/*There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.*/

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        int[] indegree = new int[numCourses];
        List<ArrayList> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int prerequisite = prerequisites[i][1];
            List temp = adj.get(prerequisite);
            temp.add(course);
            indegree[course] += 1;

        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }
        int taken = 0;
        while (queue.size() > 0) {
            int course = queue.poll();
            taken += 1;
            ArrayList<Integer> courseAdj = adj.get(course);
            for (int i = 0; i < courseAdj.size(); i++) {
                Integer c = courseAdj.get(i);
                indegree[c] -= 1;
                if (indegree[c] == 0) {
                    queue.add(c);
                }
            }
        }

        return taken == numCourses;
    }

}