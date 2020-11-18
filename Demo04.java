package day02;

import java.util.Arrays;

/**
 * 二维数组：可以看成一维的数组，数组中的元素是数组。
 */
public class Demo04 {
    public static void main(String[] args) {
        // 数组中有4个元素，每个元素是一个数组，里面有3个元素
        int[][] ids = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};

        // 效果同上
        int[][] ids2 = new int[4][3];
        ids2 = new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
        /*
        1 2 3
        4 5 6
        7 8 9
        10 11 12
         */
        System.out.println(ids[3][2]); //12
        System.out.println(Arrays.toString(ids[3])); // {10, 11, 12}

        // 遍历二维数组
        for (int i = 0; i < ids.length; i++) {
            // ids[0]  ids[1]  ids[2] ids[3]
            for (int j = 0; j < ids[i].length; j++) {
                // ids[0][0] ids[0][1] ids[0][2]
                System.out.print(ids[i][j]);
            }
            System.out.println();
        }
        // 新建一个二维数组，里面存储3个人的信息，每个人包含：姓名、年龄、身高、体重四个信息。
        String[][] persons = {{"Tom", "18", "170", "60kg"}, {"Lily", "20", "165", "50kg"}, {"AFei", "8", "150", "40kg"}};
        // 遍历二维数组：foreach的方式
        for (String[] person : persons) {
            for (String info : person) {
                System.out.print(info + "\t");
            }
            System.out.println();
        }
    }
}
