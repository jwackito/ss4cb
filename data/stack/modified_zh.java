class 栈 {
    private int[] 数据数组;
    private int 栈顶;
    private int 栈容量;

    /** 初始化一个具有给定容量的栈。 */
    public 栈(int 栈容量) {
        this.栈容量 = 栈容量;
        this.数据数组 = new int[栈容量];
        this.栈顶 = -1;
    }

    /** 如果栈中没有元素，则返回 true。 */
    public boolean 为空() {
        return 栈顶 == -1;
    }

    /** 如果栈已达到其容量，则返回 true */
    public boolean 是满的() {
        return 栈顶 == 栈容量 - 1;
    }

    /** 在栈顶部添加一个新元素。 */
    public void 压栈(int 新元素) {
        if (是满的()) {
            System.out.println("栈溢出: 无法入栈 " + 新元素);
            return;
        }
        数据数组[++栈顶] = 新元素;
    }

    /** 移除并返回栈顶元素。 */
    public int 出栈() {
        if (为空()) {
            System.out.println("栈下溢：栈为空");
            return -1;
        }
        return 数据数组[栈顶--];
    }

    /** 返回顶部元素，但不删除它。 */
    public int 取栈顶() {
        if (为空()) {
            System.out.println("栈为空");
            return -1;
        }
        return 数据数组[栈顶];
    }

    public static void main(String[] args) {
        栈 number_栈 = new 栈(5);
        number_栈.压栈(10);
        number_栈.压栈(20);
        number_栈.压栈(30);
        System.out.println("顶部元素: " + number_栈.取栈顶());
        System.out.println("已出栈: " + number_栈.出栈());
        System.out.println("已出栈: " + number_栈.出栈());
        System.out.println("是否为空: " + number_栈.为空());
    }
}
