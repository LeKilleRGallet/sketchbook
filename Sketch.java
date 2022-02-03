import java.util.Scanner;

public class Sketch{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        //create a irregular matrix
        int[][] arr2D;
        arr2D = new int[(2*n)+1][];
        for (int i = 0; i < arr2D.length; i++) {
            if (i < (n-1)) {arr2D[i] = new int[2*(i+1)];
            } else if (i == (n) || i == (n-1)) {arr2D[i] = new int[2*n];
            } else if (i > (n) && i != (2*n)) {arr2D[i] = new int[(2*(n-i)+1)+2*n];
            } else if (i == (2*n)) {arr2D[i] = new int[1];};
        }

        // fill the matrix
        for (int i = 0; i < arr2D.length; i++) {
            for (int j = 0; j < arr2D[i].length; j++) {
                if (i == 0 && j == 0) {arr2D[i][j] = m;
                } else if (i != n && j == 0) {arr2D[i][j] = (arr2D[i-1][j]+3);
                } else if (i != n && j > 0) {arr2D[i][j] = (arr2D[i][j-1]+2);
                } else if (i == n) {
                    for (int k = 0; k < i; k++){
                        try {
                            arr2D[i][j] += arr2D[k][j];
                        } catch (IndexOutOfBoundsException e) {
                            continue;
                        };
                    };
                };
        }
        } 

        for (int i = 0; i < arr2D.length; i++) {
            for (int j = 0; j < arr2D[i].length; j++) {
                System.out.print(arr2D[i][j] + "\t");
            }
            System.out.println();
        }

        sc.close();
    }
}
