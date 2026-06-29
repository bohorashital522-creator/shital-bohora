
public class statement
{
    public static void main(String[] args){
        int age;//declaartion statements 
        age = 5;//expression statements
        
        //control flow satement
        //if statement//if-else statement//if-else-if statement
        if(age > 18){
            System.out.println("Adult");
        }else if(age < 10){
            System.out.println("Minor");
        }else{
            System.out.println("Invalid age");
        }
        
        //switch statement
        int status = 200;
        switch(status){
            case 200:System.out.println("status is 200"); break;  
            case 201:System.out.println("status is 201"); break; 
            case 202:System.out.println("status is 202"); break; 
            default:System.out.println("Invalid status code"); break;
        }
        
        //loop
        //while loop
        int num = 2;
        while(num <= 3){
        System.out.println("The num is :" + num);
        num++;
    }
    //for loop
    int i = 0;
    for(i=0; i<=3; i++){
        System.out.println("This num is" + i);
    }
    //do while
    do{
        System.out.println("Once execution");
    }while(num >10);
    
    //continue
    for ( i=1; i<=10; i++){
        if(i % 2 == 0){
            continue;
        }
        System.out.println(i);
        
    }
}
}
