import java.io.*;
import java.util.*;

public class ToyStore {

    private final List<Toy> toys;
    private final List<Toy> prizeToys;

    public ToyStore() {
        this.toys = new ArrayList<>();
        this.prizeToys = new ArrayList<>();
    }

    public void addNewToy(Toy toy) {
        this.toys.add(toy);
    }

    public Toy selectPrizeToy() { // позволяет выбрать призовую игрушку в зависимости от веса игрушек,
        double totalWeight = 0;   // затем выбранная игрушка добавляется в список призовых игрушек "prizeToys"
        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }

        double randomValue = Math.random() * totalWeight;
        double currentWeight = 0;

        for (Toy toy : toys) {
            currentWeight += toy.getWeight();
            if (randomValue <= currentWeight) {
                this.prizeToys.add(toy);
                return toy;
            }
        }
        return null;
    }

    public Toy getPrizeToy() {             // удаляет первую игрушку из списка призовых игрушек,
        if (this.prizeToys.size() == 0) {  // записывает ее данные в файл и уменьшает ее количество.
            return null;
        }
        Toy prize = this.prizeToys.get(0);
        prizeToys.remove(0);
        writeToFile(prize);
        prize.decreaseQuantity();

        return prize;
    }

    private void writeToFile(Toy toy) {   // добавляет сведения об игрушке в текстовый файл
        try (FileWriter writer = new FileWriter("prize_toys.txt", true)) {
            writer.write("ID игрушки: " + toy.getToyId() + ", Название игрушки: " + toy.getName() + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}