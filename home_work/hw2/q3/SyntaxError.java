class SyntaxError extends Exception {

    private String exceptionMessage;

    public SyntaxError(String exceptionMessage){

        this.exceptionMessage = ErrorMessage;
    }
    
    @Override
    public String getLocalizedMessage(){
        
        return this.exceptionMessage;
    }
}