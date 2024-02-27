import java.util.Scanner;

public class First {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Weight in Pound: ");
        double Weight = scanner.nextDouble();

        System.out.print("Enter Height in Inches: ");
        double Height = scanner.nextDouble();

        double WeightInKg = Weight*(0.45359237);
        double HeightInM = Height*(0.0254);

        double BMI = WeightInKg/(HeightInM*HeightInM);

        System.out.print("BMI is: "  +  BMI);

    }
}
