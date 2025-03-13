import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.Text;
import javafx.scene.shape.Line;

public class BTView extends Pane {
  private BST<Integer> tree = new BST<>();
  private double radius = 15; // Tree node radius
  private double vGap = 50; // Gap between two levels in a tree

  BTView(BST<Integer> tree) {
    this.tree = tree;
    setStatus("Tree is empty");
  }

  public void setStatus(String msg) {
    getChildren().add(new Text(20, 20, msg));
  }

  public void displayTree() {
    this.getChildren().clear(); // Clear the pane
    if (tree.getRoot() != null) {
      // Display tree recursively    
      displayTree(tree.getRoot(), getWidth() / 2, vGap,
        getWidth() / 4);
    }
  }

  /** Display a subtree rooted at position (x, y) */
  private void displayTree(BST.TreeNode<Integer> root,
      double x, double y, double hGap) {
    if (root.left != null) {
      // Draw a line to the left node
      getChildren().add(new Line(x - hGap, y + vGap, x, y));
      // Draw the left subtree recursively
      displayTree(root.left, x - hGap, y + vGap, hGap / 2);
    }

    if (root.right != null) {
      // Draw a line to the right node
      getChildren().add(new Line(x + hGap, y + vGap, x, y));
      // Draw the right subtree recursively
      displayTree(root.right, x + hGap, y + vGap, hGap / 2);
    }
    
    // Display a node
    Circle circle = new Circle(x, y, radius);
    circle.setFill(Color.WHITE);
    circle.setStroke(Color.BLACK);
    getChildren().addAll(circle,
      new Text(x - 4, y + 4, root.element + ""));
  }

  public static void main(String[] args) {
    // Start the JavaFX application
    Application.launch(Main.class, args);
  }
}

class Main extends Application {
  @Override
  public void start(Stage primaryStage) {
    // Create an example BST
    BST<Integer> bst = new BST<>();
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);
    bst.insert(60);
    bst.insert(80);

    // Create the BTView to visualize the tree
    BTView btView = new BTView(bst);
    btView.setPrefSize(600, 400);
    btView.displayTree();

    // Set up the stage and scene
    StackPane root = new StackPane();
    root.getChildren().add(btView);

    Scene scene = new Scene(root, 600, 400);
    primaryStage.setTitle("Binary Tree Visualization");
    primaryStage.setScene(scene);
    primaryStage.show();
  }
}

// Example BST class (you can replace this with your existing BST class)
class BST<E extends Comparable<E>> {
  private TreeNode<E> root;

  public TreeNode<E> getRoot() {
    return root;
  }

  public void insert(E element) {
    root = insert(root, element);
  }

  private TreeNode<E> insert(TreeNode<E> node, E element) {
    if (node == null) {
      return new TreeNode<>(element);
    }

    if (element.compareTo(node.element) < 0) {
      node.left = insert(node.left, element);
    } else if (element.compareTo(node.element) > 0) {
      node.right = insert(node.right, element);
    }
    return node;
  }

  // TreeNode class for BST
  static class TreeNode<E> {
    E element;
    TreeNode<E> left;
    TreeNode<E> right;

    public TreeNode(E element) {
      this.element = element;
    }
  }
}
