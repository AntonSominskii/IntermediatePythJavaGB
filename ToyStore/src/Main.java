public class Main {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();
        store.addNewToy(new Toy("1", "Медвежонок", 10, 20.0));
        store.addNewToy(new Toy("2", "Машинка", 5, 50.0));
        store.addNewToy(new Toy("3", "Пазлы", 8, 40.0));
        store.addNewToy(new Toy("4", "Конструктор", 20, 60.0));
        store.addNewToy(new Toy("5", "Кукла", 30, 25.0));

        Toy selectedToy = store.selectPrizeToy();
        System.out.println("Выбранная игрушка в зависимости от веса: " + selectedToy.getName());

        Toy prize = store.getPrizeToy();
        System.out.println("Выданная призовая игрушка: " + prize.getName());
    }
}