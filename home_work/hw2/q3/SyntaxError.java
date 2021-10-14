class SyntaxError extends Exception {
    
    String ErrorMessage;

    // Set the Error message
    SyntaxError(String s) {
        ErrorMessage = s;
    }

    // Return the Error message
    String getErrorMessage() {
        return ErrorMessage;
    }

}