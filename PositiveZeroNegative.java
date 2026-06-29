import java.util.Scanner;
public class PositiveZeroNegative
{
    public static void main(String[] args) {
        Scanner nn = new Scanner(System.in);
        int num = nn.nextInt();
        if (num < 0 ){
            System.out.println("The number is Negative");
        }else if (num >0){
            System.out.println("The number is Positive");
        }else if (num == 0){
            System.out.println("tHe number is Zero");
        }
        
        
    }
    
}