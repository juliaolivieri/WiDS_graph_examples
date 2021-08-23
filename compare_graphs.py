import argparse
import igraph as ig
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random
import time

matplotlib.rcParams.update({'font.size': 14})

def plot_degree(g,name):
    plt.hist(g.degree())
    plt.title("{}\nDegree of vertices\nmax: {:,}, min: {:,}, median: {:,}".format(name,max(g.degree()), min(g.degree()), int(np.median(g.degree()))))
    plt.savefig("images/degree_{}.png".format(name),bbox_inches="tight")
    plt.close()

def plot_comp(g,name):
    comp_vec = g.clusters().membership
    comps = np.unique(comp_vec)
    comp_sizes = []
    for c in comps:
        comp_sizes.append(comp_vec.count(c))
    plt.hist(comp_sizes)
    plt.title("{}\nSize of components\nmax: {:,}, min: {:,}, median: {:,}".format(name,max(comp_sizes), min(comp_sizes), int(np.median(comp_sizes))))
    plt.savefig("images/comp_{}.png".format(name),bbox_inches="tight")
    plt.close()

def summarize_graph(g,t0):
    outstr = ""
    outstr += "num vertices: {:,}\n".format(g.vcount())
    print("calculated number of vertices",time.time() - t0)

    outstr += "num edges: {:,}\n".format(g.ecount())
    print("calculated number of edges",time.time() - t0)

    outstr += "diameter: {:,}\n".format(g.diameter())
    print("calculated diameter",time.time() - t0)

    outstr += "density: {:0.3f}\n".format(g.density())
    print("calculated density",time.time() - t0)

    
    # girth: length of shortest cycle
    outstr += "girth: {:,}\n".format(g.girth())
    print("calculated girth",time.time() - t0)

    
    # pearson correlation coefficient of degree between pairs of linked nodes
    outstr += "assortativity: {:0.3f}\n".format(g.assortativity_degree())
    print("calculated assortativity",time.time() - t0)

    return outstr
    

def num_comp(g):
      return str(len(set(g.clusters().membership)))

def get_edge_vert(df):
    num_vertices = len(set(df["v1"].unique()).union(df["v2"].unique()))
    num_edges = df.shape[0]
    return("vertices: {:,}, edges: {:,}".format(num_vertices, num_edges))

def get_args():
  parser = argparse.ArgumentParser(description='Get graph characteristics')
  parser.add_argument("--name", help="name of dataset", choices=["mouse_gene","web-BerkStan","facebook","twitter","movielens"])
  return parser.parse_args()


def main():
  t0 = time.time()
  args = get_args()
  print("starting",time.time() - t0)
  if args.name == "mouse_gene":
    mouse = pd.read_csv("data/bio-mouse-gene/bio-mouse-gene.edges",sep=" ",skiprows=3,names=["v1","v2","weight"])
    mouse = mouse[mouse["v1"] != mouse["v2"]]
    df = mouse

  elif args.name == "web-BerkStan":
    berkstan = pd.read_csv("data/web-BerkStan.txt",sep="\t",skiprows=4,names=["v1","v2"])
    berkstan["max"] = berkstan.max(axis=1)
    berkstan["min"] = berkstan.min(axis=1)
    berkstan.drop_duplicates(["max","min"],inplace=True)
    df = berkstan

  elif args.name == "facebook":
    sub = pd.read_csv("data/facebook/1912.edges",sep=" ", names=["v1","v2"])
    sub["max"] = sub.max(axis=1)
    sub["min"] = sub.min(axis=1)
    sub.drop_duplicates(["max","min"],inplace=True)
    df = sub


  elif args.name == "twitter":
    sub = pd.read_csv("data/twitter/16987303.edges",sep=" ", names=["v1","v2"])
    sub["max"] = sub.max(axis=1)
    sub["min"] = sub.min(axis=1)
    sub.drop_duplicates(["max","min"],inplace=True)
    df = sub

  elif args.name == "movielens":
    movielens = pd.read_csv("data/archive/tag.csv",sep=",",skiprows=1,names=["v1","v2","tag","timestamp"])
    movielens = movielens.drop_duplicates(["v1","v2"])
    movielens["v1"] = "user" + movielens["v1"].astype(str)
    movielens["v2"] = "movie" + movielens["v2"].astype(str)
    df = movielens

  print("loaded df",time.time() - t0)

  g = ig.Graph.DataFrame(df,directed=False)
  print("loaded graph",time.time() - t0)

  outfile = open("stats/{}.txt".format(args.name),"w")
  outfile.write(get_edge_vert(df) + "\n")
  print("found number of edges and vertices",time.time() - t0)
  outfile.write(num_comp(g) + "\n")
  print("found number of compartments",time.time() - t0)
  outfile.write(summarize_graph(g,t0))
  print("summarized graph",time.time() - t0)
  outfile.close()

  plot_degree(g,args.name)
  print("plotted degrees",time.time() - t0)
  plot_comp(g,args.name)
  print("plotted compartments",time.time() - t0)
main()
