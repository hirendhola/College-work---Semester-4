import java.nio.charset.StandardCharsets;
import java.util.Random;
import java.util.Scanner;

public class Third {
    public static void main(String[] args) {
        // a. Std. input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter String In Standard Input: ");
        String stdInput = scanner.nextLine();
        System.out.println("Std. Input Str: " + stdInput);

        // b. Command Line Arg
        String inputFromCmdArg = "";
        if (args.length > 0) {
            inputFromCmdArg = args[0];
            System.out.println("Command Line Arg Input Str: " + inputFromCmdArg);
        }

        // c. Length Of String
        System.out.println("Length of StdInput: " + stdInput.length());
        System.out.println("Length of CmdArgStr: " + inputFromCmdArg.length());

        // d. Reverse String
        StringBuilder reversedStr = new StringBuilder();
        for(int i = 0; i < stdInput.length(); i++){
            reversedStr.insert(0, stdInput.charAt(i));
        }
        System.out.println("Reversed Str: " + reversedStr);

        // e. copying
        String cpyStr;
        cpyStr = stdInput;

        // f. Concatenate Str
        cpyStr = cpyStr.concat(" " + inputFromCmdArg);
        System.out.println("concatenate Str: "+ cpyStr);

        // g. Extract some bytes from a string
        byte[] extBytes = cpyStr.getBytes(StandardCharsets.UTF_8);
        System.out.print("cpyStr Bytes in UTF-8: ");
        for (byte b : extBytes) {
            System.out.print(b + " ");
        }

        // h. Get Substring
        Random random = new Random();
        int randomIndexBeg = random.nextInt(cpyStr.length());
        int randomIndexEnd = random.nextInt(cpyStr.length());

        String subStr = (randomIndexBeg < randomIndexEnd) ?
                cpyStr.substring(randomIndexBeg, randomIndexEnd) :
                cpyStr.substring(randomIndexEnd, randomIndexBeg);

        System.out.println("Substring is(Random!!) for cpyStr: " + subStr);

        // i. can use  startWith/endWith java String Class method to find
        //nathi karvuuuuu....
    }
}

