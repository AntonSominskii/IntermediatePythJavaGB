public class Toy {
    private final String toyId;
    private final String name;
    private int quantity;
    private double weight;  // вес в % от 100

    public Toy(String toyId, String name, int quantity, double weight) {
        this.toyId = toyId;
        this.name = name;
        this.quantity = quantity;
        this.weight = weight;
    }

    public String getToyId() {
        return toyId;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public void decreaseQuantity() {
        if (this.quantity > 0) {
            this.quantity--;
        }
    }
}