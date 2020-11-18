package day02;

import java.util.Arrays;

/**
 * 数组：同一个类型的一组数据，使用一个名字访问。固定长度，有序排列的。
 */
public class Demo02 {
    public static void main(String[] args) {
        // 数组的定义方式一：
        int[] ids; //数组的声明
        ids = new int[]{1001, 1002, 1003}; // 数组的初始化，初始化时进行了赋值操作，数组长度是3.

        System.out.println(ids[1]); //使用下标访问第二个元素，如果下标超过数组的长度，数组越界java.lang.ArrayIndexOutOfBoundsException:
        System.out.println(ids.length); //数组的长度

        //遍历数组：foreach循环，每次取一个数组中的一个元素
        for (int a : ids) {
            System.out.println(a);
        }
        //遍历数组：遍历索引，根据索引取元素
        for (int i = 0; i < ids.length; i++) {
            System.out.println(ids[i]);
        }
        // 数组的定义方式二：
        int[] nums = new int[10]; //先声明一个数组，不赋值,10表示数组的长度。
        // 不赋值的情况下，有默认的初始值，int类型的初始值是0
        for (int n : nums) {
            System.out.println(n);
        }
        // 数组的定义方式三：
        int[] scores = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}; // 长度是10的数组，不用写new int，执行时会自动进行推断类型
        //String数组，存放人名
        String[] names = {"aa", "vv", "cc"};
        System.out.println(names); //内存地址，数组第一个元素在内存中的位置。
        for (String name : names) {
            System.out.println(name);
        }
        String[] ns = new String[10];
        // String是引用类型，引用类型的默认初始值是null。
        // int\float\double\char 是基本类型，基本类型默认初始是0值。
        for (String n : ns) {
            System.out.println(n); //打印出来为null
        }

        // 找出数组中的最大值/最小值
        // 打擂的方式
        int[] scores2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int max = scores2[0]; //将数组中第一个元素设置为max

        for (int s : scores2) {//遍历数组中的每个元素
            if (s > max) {  //如果大于max
                max = s; //将max替换
            }
        }
        System.out.println(max);

        String[] names2 = {"李思", "张三", "王五", "阿美", "张周"};
        String min = names2[0];
        for (String name : names2) {
            if (name.compareTo(min) < 0) {
                min = name;
            }
        }
        System.out.println(min);
        System.out.println("AA".compareTo("AA")); //相等返回0
        System.out.println("AA".compareTo("AB")); // -1
        System.out.println("ZB".compareTo("BA")); // 24
        System.out.println("中国".compareTo("花朵")); //-13444
        char c = '中';
        char h = '花';
        System.out.println(c - h);
        System.out.println((int) c); //打印字符对应的编码
        System.out.println((int) h);

        // 冒泡排序：由大到小排序
        int[] ss = {1, 4, 2, 5, 3, 9, 10};
        //外层控制比较的轮次
        for (int i = 0; i < ss.length; i++) {
            //内层控制比较的次数
            for (int j = 0; j < ss.length - 1; j++) {
                //比较相邻的两个元素
                if (ss[j] < ss[j + 1]) {
                    int temp;
                    temp = ss[j];
                    ss[j] = ss[j + 1];
                    ss[j + 1] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(ss));
    }


}
