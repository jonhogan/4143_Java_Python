public class RectPrism extends Rectangle{
    protected int intWidth = 0;

    //Inherits from the Rectangle class Height and Width

    RectPrism(){                    //Default constructor
        intHeight = 0;
        intLength = 0;
        intWidth = 0;
    }

    RectPrism(int h, int L, int w){   //Capital L because a lowercase one looks like a 1
        intHeight = h;                //Overrides the default constructor
        intLength = L;
        intWidth = w;
    }

    void setWidth(int w){
        intWidth = w;
    }

    @Override
    public int area(){              //Override area to work with a 3D object
        return((2*intHeight)+(2*intLength)+(2+intWidth));
    }

    int getWidth(){
        return intWidth;
    }

}