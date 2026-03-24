class スタック {
    private int[] データ配列;
    private int トップインデックス;
    private int スタック容量;

    /** 指定された容量でスタックを初期化します。 */
    public スタック(int スタック容量) {
        this.スタック容量 = スタック容量;
        this.データ配列 = new int[スタック容量];
        this.トップインデックス = -1;
    }

    /** スタックに要素がない場合はtrueを返します。 */
    public boolean 空判定() {
        return トップインデックス == -1;
    }

    /** スタックが容量に達した場合はtrueを返します。 */
    public boolean 満杯判定() {
        return トップインデックス == スタック容量 - 1;
    }

    /** スタックの一番上に新しい要素を追加します */
    public void プッシュ(int 新しい要素) {
        if (満杯判定()) {
            System.out.println("スタックオーバーフロー: プッシュできません " + 新しい要素);
            return;
        }
        データ配列[++トップインデックス] = 新しい要素;
    }

    /** スタックの最上位要素を削除して返します。 */
    public int ポップ() {
        if (空判定()) {
            System.out.println("スタックアンダーフロー: スタックが空です");
            return -1;
        }
        return データ配列[トップインデックス--];
    }

    /** 最上位要素を削除せずに返します。 */
    public int ピーク() {
        if (空判定()) {
            System.out.println("スタックは空判定");
            return -1;
        }
        return データ配列[トップインデックス];
    }

    public static void main(String[] args) {
        スタック 番号スタック = new スタック(5);
        番号スタック.プッシュ(10);
        番号スタック.プッシュ(20);
        番号スタック.プッシュ(30);
        System.out.println("上部要素: " + 番号スタック.ピーク());
        System.out.println("取り出された: " + 番号スタック.ポップ());
        System.out.println("取り出された: " + 番号スタック.ポップ());
        System.out.println("空判定: " + 番号スタック.空判定());
    }
}
