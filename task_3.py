import java.util.Scanner;

class Main {
    private double balance;
    private Scanner scanner;

    public Main(double balance) {
        this.balance = balance;
        this.scanner = new Scanner(System.in);
    }

    public void run() {
        while (true) {
            System.out.println("\nATM Menu:");
            System.out.println("1. Withdraw");
            System.out.println("2. Deposit");
            System.out.println("3. Check Balance");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    withdraw();
                    break;
                case 2:
                    deposit();
                    break;
                case 3:
                    checkBalance();
                    break;
                case 4:
                    System.out.println("Exiting ATM.");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private void withdraw() {
        System.out.print("Enter withdrawal amount: ");
        double amount = scanner.nextDouble();
        if (amount > balance) {
            System.out.println("Insufficient balance.");
        } else {
            balance -= amount;
            System.out.printf("Withdrawal successful. New balance: %.2f%n", balance);
        }
    }

    private void deposit() {
        System.out.print("Enter deposit amount: ");
        double amount = scanner.nextDouble();
        balance += amount;
        System.out.printf("Deposit successful. New balance: %.2f%n", balance);
    }

    private void checkBalance() {
        System.out.printf("Current balance: %.2f%n", balance);
    }

    public static void main(String[] args) {
        Main atm = new Main(0);
        atm.run();
    }
}
