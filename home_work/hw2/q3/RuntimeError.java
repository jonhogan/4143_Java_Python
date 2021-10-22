public class RuntimeError extends Exception {

        String ErrorMessage;
    
        // Set the Error message
        RuntimeError(String s) {
            ErrorMessage = s;
        }
    
        // Return the Error message
        String getErrorMessage() {
            return ErrorMessage;
        }
}
