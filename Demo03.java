package day02;

import java.util.Arrays;

/**
 * 数组的工具类：Arrays，封装了一些方法，方便操作数组。
 */
public class Demo03 {
    public static void main(String[] args) {
        // Arrays是类名
        int[] ids = {1001, 10012, 1002, 10013, 1004};
        System.out.println("排序前：" + Arrays.toString(ids)); //Arrays.toString将数组转成字符串
        Arrays.sort(ids); //数组排序
        System.out.println("排序后：" + Arrays.toString(ids));//[1001, 1002, 1004, 10012, 10013]

        // 二分查找，第一个参数是一个升序的数组。
        // [1001, 1002, 1004, 10012, 10013]
        // 1004 10012
        int index = Arrays.binarySearch(ids, 10012); // 如果存在，返回在数组中的索引
        System.out.println(index);

        index = Arrays.binarySearch(ids, 1005); // -4 1005如果存在数组中，它的索引是3，返回的结果：-(3+1)
        System.out.println(index);

        int[] newIds = Arrays.copyOf(ids, 3);  //数组的扩容、缩容
        System.out.println(Arrays.toString(newIds));

        boolean isEqual = Arrays.equals(ids, newIds); //比较数组是否相等
        System.out.println(isEqual);
    }
}
