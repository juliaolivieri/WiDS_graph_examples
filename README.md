# Real Graph Examples
## Workshop information

This repository contains the code for the WiDS lecture "Graph Theory for Data Science, Part III: Characterizing graphs in the real world":

Many of the systems we study today can be represented as graphs, from social media networks to phylogenetic trees to airplane flight paths. In this workshop we will explore real-world examples of graphs, discussing how to extract graphs from real data, data structures for storing graphs, and measures to characterize graphs. We will work with real examples of graph data to create a table of values that summarize different example graphs, exploring values such as the centrality, assortativity, and diameter of each graph. Python code will be provided so that attendees can get hands-on experience analyzing graph data.

Previous lectures: 

[Graph Theory for Data Science, Part I: What is a graph and what can we do with it?](https://www.youtube.com/watch?v=KlzWjdaXYgA&list=PLHAk3jHXWpxI7fHw8m5PhrpSRpR3NIjQo&index=1)

[Graph Theory for Data Science, Part II: Graph Algorithms: Traversing the tree and beyond](https://www.youtube.com/watch?v=45jNuN4DtPM&list=PLHAk3jHXWpxI7fHw8m5PhrpSRpR3NIjQo&index=3) | [code for workshop](https://github.com/juliaolivieri/WiDS_graph_algorithms)

Lecturer: Julia Olivieri (jolivier@stanford.edu)

## Running the code
Clone this repo and enter the folder:

    $ git clone https://github.com/juliaolivieri/WiDS_graph_examples.git
    $ cd WiDS_graph_examples/

Install any missing requirements with the following command (note that this will install the Python packages numpy, matplotlib, networkx, pandas, python-igraph, and jupyterlab):

    $ pip install -r requirements.txt

You can create a virtual environment if you don't want to install these packages in your base environment:

    $ conda env create -n wids_graph -f environment.yml

And activate it:

    $ source activate wids_graph

Once you have the required packages installed, start a jupyter notebook:

    $ jupyter notebook

Open the python notebook `Compare_Graphs.ipynb`. Run every cell (you can run a cell by pressing Shift and Enter while it is selected). 

You can change the number of nodes each graph is subsetted to by changing the `num_nodes` variable. You can also try calculating additional metrics for the graphs.

## Links mentioned in the lecture
* Relation between adjacency matrix and number of random walks proof: [https://people.cs.clemson.edu/~goddard/handouts/math8540/adjacencyNotes.pdf](https://people.cs.clemson.edu/~goddard/handouts/math8540/adjacencyNotes.pdf)
* Further reading on the graph Laplacian: [https://mbernste.github.io/posts/laplacian_matrix/](https://mbernste.github.io/posts/laplacian_matrix/)

## Links to download all analyzed datasets
* `twitter`: [https://snap.stanford.edu/data/ego-Twitter.html](https://snap.stanford.edu/data/ego-Twitter.html)

* `facebook`: [https://snap.stanford.edu/data/ego-Facebook.html](https://snap.stanford.edu/data/ego-Facebook.html)

* `movielens`: [https://www.kaggle.com/grouplens/movielens-20m-dataset](https://www.kaggle.com/grouplens/movielens-20m-dataset)

* `mouse-gene`: [https://networkrepository.com/bio-mouse-gene.php](https://networkrepository.com/bio-mouse-gene.php)

* `web-BerkStan`: [https://snap.stanford.edu/data/web-BerkStan.html](https://snap.stanford.edu/data/web-BerkStan.html)

