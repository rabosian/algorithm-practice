import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {
    public static void main(String args[]) {
        int[] nums = {1,5,4,2,7};
        int target = 12;
        int[] result = twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }

    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();

        for(int i=0; i < nums.length; i++){
            Integer diff = target - nums[i];
            if(hashMap.containsKey(diff)) {
                int[] result = {hashMap.get(diff), i};
                return result;
            }
            // key, value -> num, index
            hashMap.put(nums[i], i);
        }
        return null;
    }
}