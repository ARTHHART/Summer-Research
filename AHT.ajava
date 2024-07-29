
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.jlab.groot.data.GraphErrors;
import org.jlab.groot.data.H2F;
import org.jlab.groot.graphics.EmbeddedCanvas;

class Particle {
    int pid;
    float px, py, pz, energy;

    public Particle(int pid, float px, float py, float pz, float energy) {
        this.pid = pid;
        this.px = px;
        this.py = py;
        this.pz = pz;
        this.energy = energy;
    }

    @Override
    public String toString() {
        return "Particle [pid=" + pid + ", px=" + px + ", py=" + py + ", pz=" + pz + ", energy=" + energy + "]";
    }
}

public class AHT {
    public static void main(String[] args) {
        // Print the current working directory
        System.out.println("Current working directory: " + System.getProperty("user.dir"));

        // Use an absolute path to the file
        String filePath = "/home/hartel1/GiBUU/release/testRun/output2.txt"; // Update this to your actual file path

        List<Particle> particles = new ArrayList<>();
        List<Double> betaValues = new ArrayList<>();
        List<Double> momentumValues = new ArrayList<>();
        List<Double> deltaBetaValues = new ArrayList<>();
        Map<Integer, Integer> pidColorMap = new HashMap<>(); // Map to store color mapping for different PIDs
        int colorIndex = 1; // Index for assigning colors, starting from 1 to avoid default black color
        H2F BVM = new H2F("BVM", "BVM", 100, 0,5, 100, 0, 1.2 );
        H2F BVM311 = new H2F("BVM311", "BVM311", 100, 0,5, 100, 0, 1.2 );
        H2F DBVM = new H2F("DBVM", "DBVM", 100, 0,5, 100, -0.1, 0.1 );
        H2F DBVM311 = new H2F("DBVM311", "DBVM311", 100, 0,5, 100, -0.1, 0.1 );
        // Read the file and store particle data
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.trim();
                // Skip lines that are not particle data
                if (line.startsWith("Particle ID:")) {
                    // Extract particle data
                    String[] parts = line.split(",");
                    int pid = (int) Double.parseDouble(parts[0].split(":")[1].trim());
                    float px = Float.parseFloat(parts[2].split(":")[1].trim());
                    float py = Float.parseFloat(parts[3].split(":")[1].trim());
                    float pz = Float.parseFloat(parts[4].split(":")[1].trim());
                    float energy = Float.parseFloat(parts[5].split(":")[1].trim());
                    Particle particle = new Particle(pid, px, py, pz, energy);
                    particles.add(particle);

                    // Calculate momentum and beta

                        double momentum = Math.sqrt((px * px) + (py * py) + (pz * pz));
                        double beta = momentum / energy;
                        BVM.fill(momentum, beta);
                        momentumValues.add(momentum);
                        betaValues.add(beta);

                        // Calculate delta beta for protons
                        double referenceBeta = momentum / Math.sqrt(momentum * momentum + 0.938 * 0.938); // Using proton mass of 0.938 GeV/c^2
                        double deltaBeta = beta - referenceBeta;
                        DBVM.fill(momentum, deltaBeta);
                        deltaBetaValues.add(deltaBeta);
                    if (pid == 311){
                        BVM311.fill(momentum, beta);
                        DBVM311.fill(momentum, deltaBeta);
                    }

                    // Store color for each PID if not already stored
                    if (!pidColorMap.containsKey(pid)) {
                        pidColorMap.put(pid, colorIndex);
                        colorIndex++;
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Print all particles read
        for (Particle particle : particles) {
            System.out.println(particle);
        }

        // Create the Momentum vs Beta graph
        /*GraphErrors graphMomentumBeta = new GraphErrors("Momentum vs Beta");

        // Add data to the graph with different colors for different PIDs
        for (int i = 0; i < momentumValues.size(); i++) {
            int pid = particles.get(i).pid;
            int color = pidColorMap.get(pid);
            graphMomentumBeta.addPoint(momentumValues.get(i), betaValues.get(i), 0, 0);
            graphMomentumBeta.setMarkerColor(i); // Set the color for the point
        }

        // Set axis titles for Momentum vs Beta graph
        graphMomentumBeta.setTitleX("Momentum (GeV/c)");
        graphMomentumBeta.setTitleY("Beta");

        // Set marker style for Momentum vs Beta graph
        graphMomentumBeta.setMarkerStyle(1);
        graphMomentumBeta.setMarkerSize(5);

        // Create the Delta Beta vs Momentum graph for protons
        GraphErrors graphDeltaBetaMomentum = new GraphErrors("Delta Beta vs Momentum (Protons)");

        // Add data to the Delta Beta vs Momentum graph
        for (int i = 0; i < deltaBetaValues.size(); i++) {
            graphDeltaBetaMomentum.addPoint(momentumValues.get(i), deltaBetaValues.get(i), 0, 0);
            graphDeltaBetaMomentum.setMarkerColor(i); // Using color index 2 for protons
        }

        // Set axis titles for Delta Beta vs Momentum graph
        graphDeltaBetaMomentum.setTitleX("Momentum (GeV/c)");
        graphDeltaBetaMomentum.setTitleY("Delta Beta");

        // Set marker style for Delta Beta vs Momentum graph
        graphDeltaBetaMomentum.setMarkerStyle(1);
        graphDeltaBetaMomentum.setMarkerSize(5);
        */
        // Create a canvas for the Momentum vs Beta graph
        EmbeddedCanvas canvasMomentumBeta = new EmbeddedCanvas();
        canvasMomentumBeta.setSize(800, 600);
        canvasMomentumBeta.draw(BVM);
        canvasMomentumBeta.save("momentum_vs_beta.png"); // Save the plot as an image

        // Display the Momentum vs Beta graph in a JFrame
        javax.swing.JFrame frameMomentumBeta = new javax.swing.JFrame("Momentum vs Beta");
        frameMomentumBeta.setSize(800, 600);
        frameMomentumBeta.add(canvasMomentumBeta);
        frameMomentumBeta.setLocationRelativeTo(null);
        frameMomentumBeta.setVisible(true);
        frameMomentumBeta.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);

        EmbeddedCanvas canvasMomentumBeta1 = new EmbeddedCanvas();
        canvasMomentumBeta1.setSize(800, 600);
        canvasMomentumBeta1.draw(BVM311);
        canvasMomentumBeta1.save("momentum_vs_beta.png"); // Save the plot as an image

        // Display the Momentum vs Beta graph in a JFrame
        javax.swing.JFrame frameMomentumBeta1 = new javax.swing.JFrame("Momentum vs Beta");
        frameMomentumBeta1.setSize(800, 600);
        frameMomentumBeta1.add(canvasMomentumBeta1);
        frameMomentumBeta1.setLocationRelativeTo(null);
        frameMomentumBeta1.setVisible(true);
        frameMomentumBeta1.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
        // Create a canvas for the Delta Beta vs Momentum graph

        EmbeddedCanvas canvasDeltaBetaMomentum = new EmbeddedCanvas();
        canvasDeltaBetaMomentum.setSize(800, 600);
        canvasDeltaBetaMomentum.draw(DBVM);
        canvasDeltaBetaMomentum.save("delta_beta_vs_momentum.png"); // Save the plot as an image

        // Display the Delta Beta vs Momentum graph in a JFrame
        javax.swing.JFrame frameDeltaBetaMomentum = new javax.swing.JFrame("Delta Beta vs Momentum (Protons)");
        frameDeltaBetaMomentum.setSize(800, 600);
        frameDeltaBetaMomentum.add(canvasDeltaBetaMomentum);
        frameDeltaBetaMomentum.setLocationRelativeTo(null);
        frameDeltaBetaMomentum.setVisible(true);
        frameDeltaBetaMomentum.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);

        EmbeddedCanvas canvasDeltaBetaMomentum1 = new EmbeddedCanvas();
        canvasDeltaBetaMomentum1.setSize(800, 600);
        canvasDeltaBetaMomentum1.draw(DBVM311);
        canvasDeltaBetaMomentum1.save("delta_beta_vs_momentum.png"); // Save the plot as an image

        // Display the Delta Beta vs Momentum graph in a JFrame
        javax.swing.JFrame frameDeltaBetaMomentum1 = new javax.swing.JFrame("Delta Beta vs Momentum (Protons)");
        frameDeltaBetaMomentum1.setSize(800, 600);
        frameDeltaBetaMomentum1.add(canvasDeltaBetaMomentum1);
        frameDeltaBetaMomentum1.setLocationRelativeTo(null);
        frameDeltaBetaMomentum1.setVisible(true);
        frameDeltaBetaMomentum1.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
    }
}
