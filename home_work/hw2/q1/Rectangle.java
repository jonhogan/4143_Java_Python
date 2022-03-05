public class Rectangle{

    protected int intHeight;
    protected int intLength;

    Rectangle(){                    //Default constructor
        intHeight = 0;
        intLength = 0;
    }

    Rectangle(int h, int L){        //Overrides the default constructor
        intHeight = h;
        intLength = L;
    }
    
    //Following two methods implements encapsulation
    //with the protected variables
    public void setHeight(int h){
        intHeight = h;
    }

    public void setLength(int L){
        intLength = L;
    }

    public int area(){
        return intHeight*intLength;
    }

    int getLength(){
        return intLength;
    }

    int getHeight(){
        return intHeight;
    }

}
