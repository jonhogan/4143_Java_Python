class RuntimeError extends Exception{

    private String exceptionMessage;

    public RuntimeError(String exceptionMessage){

        this.exceptionMessage = exceptionMessage;
    }

    @Override
    public String getLocalizedMessage(){

        return  this.exceptionMessage+"\n";
    }
}