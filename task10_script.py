import pymol
from pymol import cmd

cmd.fetch("2GJX")
cmd.fetch("2GK1")

# 1
cmd.create("chain_A", "2GJX and chain A")
cmd.create("chain_B", "2GJX and chain B")
cmd.hide("everything", "2GJX")
cmd.orient("chain_A or chain_B")
cmd.png("task9_img1_py.png")

# 2
cmd.color("yellow", "chain_A")
cmd.color("blue", "chain_B")
cmd.png("task9_img2_py.png")

# 3
cmd.hide("cartoon", "chain_A or chain_B")
cmd.show("surface", "chain_A")
cmd.show("licorice", "chain_B")
cmd.png("task9_img3_py.png")

# 4
cmd.create("chain_I", "2GK1 and chain I")
cmd.color("green", "chain_I")
cmd.hide("everything", "2GK1")
cmd.hide("everything", "chain_A")
cmd.hide("licorice", "chain_B")
cmd.show("cartoon", "chain_B")
cmd.align("chain_I", "chain_B")
cmd.zoom("visible")
cmd.png("task9_img4_py.png")
