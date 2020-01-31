Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = [12, 50, 98, 100]
>>> F = [t * 1.8 + 32 for t in T]
>>> F
[53.6, 122.0, 208.4, 212.0]
>>> def c2f(t):
	return t * 1.8 + 32

>>> F = []
>>> for t in T:
	F.append(c2f(t))

	
>>> F
[53.6, 122.0, 208.4, 212.0]
>>> F = map(c2f, T)
>>> F
<map object at 0x000001ECE83FEF60>
>>> list(F)
[53.6, 122.0, 208.4, 212.0]
>>> ############################################
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> 
>>> def fil(n):
	if(n % 5 == 0 and n % 8 == 0):
		return True
	else:
		return False

	
>>> filter(fil, L)
<filter object at 0x000001ECE83FEF98>
>>> list(filter(fil, L))
[0, 40, 80]
>>> ###################################################
>>> T1 = ('Anil', 'Sunil', 'Suresh')
>>> T2 = (35, 37, 38)
>>> zip(T1, T2)
<zip object at 0x000001ECE84274C8>
>>> list(zip(T1, T2))
[('Anil', 35), ('Sunil', 37), ('Suresh', 38)]
>>> #####################################################
>>> T= tuple([('Anil', 35), ('Sunil', 37), ('Suresh', 38)])
>>> T
(('Anil', 35), ('Sunil', 37), ('Suresh', 38))
>>> # How to unzip the tuple T?
>>> 
>>> #####################################################
>>> 
>>> L = [(x,y) for x in range(100) for y in range(100) if (x + y) % 8 == 0]
>>> L
[(0, 0), (0, 8), (0, 16), (0, 24), (0, 32), (0, 40), (0, 48), (0, 56), (0, 64), (0, 72), (0, 80), (0, 88), (0, 96), (1, 7), (1, 15), (1, 23), (1, 31), (1, 39), (1, 47), (1, 55), (1, 63), (1, 71), (1, 79), (1, 87), (1, 95), (2, 6), (2, 14), (2, 22), (2, 30), (2, 38), (2, 46), (2, 54), (2, 62), (2, 70), (2, 78), (2, 86), (2, 94), (3, 5), (3, 13), (3, 21), (3, 29), (3, 37), (3, 45), (3, 53), (3, 61), (3, 69), (3, 77), (3, 85), (3, 93), (4, 4), (4, 12), (4, 20), (4, 28), (4, 36), (4, 44), (4, 52), (4, 60), (4, 68), (4, 76), (4, 84), (4, 92), (5, 3), (5, 11), (5, 19), (5, 27), (5, 35), (5, 43), (5, 51), (5, 59), (5, 67), (5, 75), (5, 83), (5, 91), (5, 99), (6, 2), (6, 10), (6, 18), (6, 26), (6, 34), (6, 42), (6, 50), (6, 58), (6, 66), (6, 74), (6, 82), (6, 90), (6, 98), (7, 1), (7, 9), (7, 17), (7, 25), (7, 33), (7, 41), (7, 49), (7, 57), (7, 65), (7, 73), (7, 81), (7, 89), (7, 97), (8, 0), (8, 8), (8, 16), (8, 24), (8, 32), (8, 40), (8, 48), (8, 56), (8, 64), (8, 72), (8, 80), (8, 88), (8, 96), (9, 7), (9, 15), (9, 23), (9, 31), (9, 39), (9, 47), (9, 55), (9, 63), (9, 71), (9, 79), (9, 87), (9, 95), (10, 6), (10, 14), (10, 22), (10, 30), (10, 38), (10, 46), (10, 54), (10, 62), (10, 70), (10, 78), (10, 86), (10, 94), (11, 5), (11, 13), (11, 21), (11, 29), (11, 37), (11, 45), (11, 53), (11, 61), (11, 69), (11, 77), (11, 85), (11, 93), (12, 4), (12, 12), (12, 20), (12, 28), (12, 36), (12, 44), (12, 52), (12, 60), (12, 68), (12, 76), (12, 84), (12, 92), (13, 3), (13, 11), (13, 19), (13, 27), (13, 35), (13, 43), (13, 51), (13, 59), (13, 67), (13, 75), (13, 83), (13, 91), (13, 99), (14, 2), (14, 10), (14, 18), (14, 26), (14, 34), (14, 42), (14, 50), (14, 58), (14, 66), (14, 74), (14, 82), (14, 90), (14, 98), (15, 1), (15, 9), (15, 17), (15, 25), (15, 33), (15, 41), (15, 49), (15, 57), (15, 65), (15, 73), (15, 81), (15, 89), (15, 97), (16, 0), (16, 8), (16, 16), (16, 24), (16, 32), (16, 40), (16, 48), (16, 56), (16, 64), (16, 72), (16, 80), (16, 88), (16, 96), (17, 7), (17, 15), (17, 23), (17, 31), (17, 39), (17, 47), (17, 55), (17, 63), (17, 71), (17, 79), (17, 87), (17, 95), (18, 6), (18, 14), (18, 22), (18, 30), (18, 38), (18, 46), (18, 54), (18, 62), (18, 70), (18, 78), (18, 86), (18, 94), (19, 5), (19, 13), (19, 21), (19, 29), (19, 37), (19, 45), (19, 53), (19, 61), (19, 69), (19, 77), (19, 85), (19, 93), (20, 4), (20, 12), (20, 20), (20, 28), (20, 36), (20, 44), (20, 52), (20, 60), (20, 68), (20, 76), (20, 84), (20, 92), (21, 3), (21, 11), (21, 19), (21, 27), (21, 35), (21, 43), (21, 51), (21, 59), (21, 67), (21, 75), (21, 83), (21, 91), (21, 99), (22, 2), (22, 10), (22, 18), (22, 26), (22, 34), (22, 42), (22, 50), (22, 58), (22, 66), (22, 74), (22, 82), (22, 90), (22, 98), (23, 1), (23, 9), (23, 17), (23, 25), (23, 33), (23, 41), (23, 49), (23, 57), (23, 65), (23, 73), (23, 81), (23, 89), (23, 97), (24, 0), (24, 8), (24, 16), (24, 24), (24, 32), (24, 40), (24, 48), (24, 56), (24, 64), (24, 72), (24, 80), (24, 88), (24, 96), (25, 7), (25, 15), (25, 23), (25, 31), (25, 39), (25, 47), (25, 55), (25, 63), (25, 71), (25, 79), (25, 87), (25, 95), (26, 6), (26, 14), (26, 22), (26, 30), (26, 38), (26, 46), (26, 54), (26, 62), (26, 70), (26, 78), (26, 86), (26, 94), (27, 5), (27, 13), (27, 21), (27, 29), (27, 37), (27, 45), (27, 53), (27, 61), (27, 69), (27, 77), (27, 85), (27, 93), (28, 4), (28, 12), (28, 20), (28, 28), (28, 36), (28, 44), (28, 52), (28, 60), (28, 68), (28, 76), (28, 84), (28, 92), (29, 3), (29, 11), (29, 19), (29, 27), (29, 35), (29, 43), (29, 51), (29, 59), (29, 67), (29, 75), (29, 83), (29, 91), (29, 99), (30, 2), (30, 10), (30, 18), (30, 26), (30, 34), (30, 42), (30, 50), (30, 58), (30, 66), (30, 74), (30, 82), (30, 90), (30, 98), (31, 1), (31, 9), (31, 17), (31, 25), (31, 33), (31, 41), (31, 49), (31, 57), (31, 65), (31, 73), (31, 81), (31, 89), (31, 97), (32, 0), (32, 8), (32, 16), (32, 24), (32, 32), (32, 40), (32, 48), (32, 56), (32, 64), (32, 72), (32, 80), (32, 88), (32, 96), (33, 7), (33, 15), (33, 23), (33, 31), (33, 39), (33, 47), (33, 55), (33, 63), (33, 71), (33, 79), (33, 87), (33, 95), (34, 6), (34, 14), (34, 22), (34, 30), (34, 38), (34, 46), (34, 54), (34, 62), (34, 70), (34, 78), (34, 86), (34, 94), (35, 5), (35, 13), (35, 21), (35, 29), (35, 37), (35, 45), (35, 53), (35, 61), (35, 69), (35, 77), (35, 85), (35, 93), (36, 4), (36, 12), (36, 20), (36, 28), (36, 36), (36, 44), (36, 52), (36, 60), (36, 68), (36, 76), (36, 84), (36, 92), (37, 3), (37, 11), (37, 19), (37, 27), (37, 35), (37, 43), (37, 51), (37, 59), (37, 67), (37, 75), (37, 83), (37, 91), (37, 99), (38, 2), (38, 10), (38, 18), (38, 26), (38, 34), (38, 42), (38, 50), (38, 58), (38, 66), (38, 74), (38, 82), (38, 90), (38, 98), (39, 1), (39, 9), (39, 17), (39, 25), (39, 33), (39, 41), (39, 49), (39, 57), (39, 65), (39, 73), (39, 81), (39, 89), (39, 97), (40, 0), (40, 8), (40, 16), (40, 24), (40, 32), (40, 40), (40, 48), (40, 56), (40, 64), (40, 72), (40, 80), (40, 88), (40, 96), (41, 7), (41, 15), (41, 23), (41, 31), (41, 39), (41, 47), (41, 55), (41, 63), (41, 71), (41, 79), (41, 87), (41, 95), (42, 6), (42, 14), (42, 22), (42, 30), (42, 38), (42, 46), (42, 54), (42, 62), (42, 70), (42, 78), (42, 86), (42, 94), (43, 5), (43, 13), (43, 21), (43, 29), (43, 37), (43, 45), (43, 53), (43, 61), (43, 69), (43, 77), (43, 85), (43, 93), (44, 4), (44, 12), (44, 20), (44, 28), (44, 36), (44, 44), (44, 52), (44, 60), (44, 68), (44, 76), (44, 84), (44, 92), (45, 3), (45, 11), (45, 19), (45, 27), (45, 35), (45, 43), (45, 51), (45, 59), (45, 67), (45, 75), (45, 83), (45, 91), (45, 99), (46, 2), (46, 10), (46, 18), (46, 26), (46, 34), (46, 42), (46, 50), (46, 58), (46, 66), (46, 74), (46, 82), (46, 90), (46, 98), (47, 1), (47, 9), (47, 17), (47, 25), (47, 33), (47, 41), (47, 49), (47, 57), (47, 65), (47, 73), (47, 81), (47, 89), (47, 97), (48, 0), (48, 8), (48, 16), (48, 24), (48, 32), (48, 40), (48, 48), (48, 56), (48, 64), (48, 72), (48, 80), (48, 88), (48, 96), (49, 7), (49, 15), (49, 23), (49, 31), (49, 39), (49, 47), (49, 55), (49, 63), (49, 71), (49, 79), (49, 87), (49, 95), (50, 6), (50, 14), (50, 22), (50, 30), (50, 38), (50, 46), (50, 54), (50, 62), (50, 70), (50, 78), (50, 86), (50, 94), (51, 5), (51, 13), (51, 21), (51, 29), (51, 37), (51, 45), (51, 53), (51, 61), (51, 69), (51, 77), (51, 85), (51, 93), (52, 4), (52, 12), (52, 20), (52, 28), (52, 36), (52, 44), (52, 52), (52, 60), (52, 68), (52, 76), (52, 84), (52, 92), (53, 3), (53, 11), (53, 19), (53, 27), (53, 35), (53, 43), (53, 51), (53, 59), (53, 67), (53, 75), (53, 83), (53, 91), (53, 99), (54, 2), (54, 10), (54, 18), (54, 26), (54, 34), (54, 42), (54, 50), (54, 58), (54, 66), (54, 74), (54, 82), (54, 90), (54, 98), (55, 1), (55, 9), (55, 17), (55, 25), (55, 33), (55, 41), (55, 49), (55, 57), (55, 65), (55, 73), (55, 81), (55, 89), (55, 97), (56, 0), (56, 8), (56, 16), (56, 24), (56, 32), (56, 40), (56, 48), (56, 56), (56, 64), (56, 72), (56, 80), (56, 88), (56, 96), (57, 7), (57, 15), (57, 23), (57, 31), (57, 39), (57, 47), (57, 55), (57, 63), (57, 71), (57, 79), (57, 87), (57, 95), (58, 6), (58, 14), (58, 22), (58, 30), (58, 38), (58, 46), (58, 54), (58, 62), (58, 70), (58, 78), (58, 86), (58, 94), (59, 5), (59, 13), (59, 21), (59, 29), (59, 37), (59, 45), (59, 53), (59, 61), (59, 69), (59, 77), (59, 85), (59, 93), (60, 4), (60, 12), (60, 20), (60, 28), (60, 36), (60, 44), (60, 52), (60, 60), (60, 68), (60, 76), (60, 84), (60, 92), (61, 3), (61, 11), (61, 19), (61, 27), (61, 35), (61, 43), (61, 51), (61, 59), (61, 67), (61, 75), (61, 83), (61, 91), (61, 99), (62, 2), (62, 10), (62, 18), (62, 26), (62, 34), (62, 42), (62, 50), (62, 58), (62, 66), (62, 74), (62, 82), (62, 90), (62, 98), (63, 1), (63, 9), (63, 17), (63, 25), (63, 33), (63, 41), (63, 49), (63, 57), (63, 65), (63, 73), (63, 81), (63, 89), (63, 97), (64, 0), (64, 8), (64, 16), (64, 24), (64, 32), (64, 40), (64, 48), (64, 56), (64, 64), (64, 72), (64, 80), (64, 88), (64, 96), (65, 7), (65, 15), (65, 23), (65, 31), (65, 39), (65, 47), (65, 55), (65, 63), (65, 71), (65, 79), (65, 87), (65, 95), (66, 6), (66, 14), (66, 22), (66, 30), (66, 38), (66, 46), (66, 54), (66, 62), (66, 70), (66, 78), (66, 86), (66, 94), (67, 5), (67, 13), (67, 21), (67, 29), (67, 37), (67, 45), (67, 53), (67, 61), (67, 69), (67, 77), (67, 85), (67, 93), (68, 4), (68, 12), (68, 20), (68, 28), (68, 36), (68, 44), (68, 52), (68, 60), (68, 68), (68, 76), (68, 84), (68, 92), (69, 3), (69, 11), (69, 19), (69, 27), (69, 35), (69, 43), (69, 51), (69, 59), (69, 67), (69, 75), (69, 83), (69, 91), (69, 99), (70, 2), (70, 10), (70, 18), (70, 26), (70, 34), (70, 42), (70, 50), (70, 58), (70, 66), (70, 74), (70, 82), (70, 90), (70, 98), (71, 1), (71, 9), (71, 17), (71, 25), (71, 33), (71, 41), (71, 49), (71, 57), (71, 65), (71, 73), (71, 81), (71, 89), (71, 97), (72, 0), (72, 8), (72, 16), (72, 24), (72, 32), (72, 40), (72, 48), (72, 56), (72, 64), (72, 72), (72, 80), (72, 88), (72, 96), (73, 7), (73, 15), (73, 23), (73, 31), (73, 39), (73, 47), (73, 55), (73, 63), (73, 71), (73, 79), (73, 87), (73, 95), (74, 6), (74, 14), (74, 22), (74, 30), (74, 38), (74, 46), (74, 54), (74, 62), (74, 70), (74, 78), (74, 86), (74, 94), (75, 5), (75, 13), (75, 21), (75, 29), (75, 37), (75, 45), (75, 53), (75, 61), (75, 69), (75, 77), (75, 85), (75, 93), (76, 4), (76, 12), (76, 20), (76, 28), (76, 36), (76, 44), (76, 52), (76, 60), (76, 68), (76, 76), (76, 84), (76, 92), (77, 3), (77, 11), (77, 19), (77, 27), (77, 35), (77, 43), (77, 51), (77, 59), (77, 67), (77, 75), (77, 83), (77, 91), (77, 99), (78, 2), (78, 10), (78, 18), (78, 26), (78, 34), (78, 42), (78, 50), (78, 58), (78, 66), (78, 74), (78, 82), (78, 90), (78, 98), (79, 1), (79, 9), (79, 17), (79, 25), (79, 33), (79, 41), (79, 49), (79, 57), (79, 65), (79, 73), (79, 81), (79, 89), (79, 97), (80, 0), (80, 8), (80, 16), (80, 24), (80, 32), (80, 40), (80, 48), (80, 56), (80, 64), (80, 72), (80, 80), (80, 88), (80, 96), (81, 7), (81, 15), (81, 23), (81, 31), (81, 39), (81, 47), (81, 55), (81, 63), (81, 71), (81, 79), (81, 87), (81, 95), (82, 6), (82, 14), (82, 22), (82, 30), (82, 38), (82, 46), (82, 54), (82, 62), (82, 70), (82, 78), (82, 86), (82, 94), (83, 5), (83, 13), (83, 21), (83, 29), (83, 37), (83, 45), (83, 53), (83, 61), (83, 69), (83, 77), (83, 85), (83, 93), (84, 4), (84, 12), (84, 20), (84, 28), (84, 36), (84, 44), (84, 52), (84, 60), (84, 68), (84, 76), (84, 84), (84, 92), (85, 3), (85, 11), (85, 19), (85, 27), (85, 35), (85, 43), (85, 51), (85, 59), (85, 67), (85, 75), (85, 83), (85, 91), (85, 99), (86, 2), (86, 10), (86, 18), (86, 26), (86, 34), (86, 42), (86, 50), (86, 58), (86, 66), (86, 74), (86, 82), (86, 90), (86, 98), (87, 1), (87, 9), (87, 17), (87, 25), (87, 33), (87, 41), (87, 49), (87, 57), (87, 65), (87, 73), (87, 81), (87, 89), (87, 97), (88, 0), (88, 8), (88, 16), (88, 24), (88, 32), (88, 40), (88, 48), (88, 56), (88, 64), (88, 72), (88, 80), (88, 88), (88, 96), (89, 7), (89, 15), (89, 23), (89, 31), (89, 39), (89, 47), (89, 55), (89, 63), (89, 71), (89, 79), (89, 87), (89, 95), (90, 6), (90, 14), (90, 22), (90, 30), (90, 38), (90, 46), (90, 54), (90, 62), (90, 70), (90, 78), (90, 86), (90, 94), (91, 5), (91, 13), (91, 21), (91, 29), (91, 37), (91, 45), (91, 53), (91, 61), (91, 69), (91, 77), (91, 85), (91, 93), (92, 4), (92, 12), (92, 20), (92, 28), (92, 36), (92, 44), (92, 52), (92, 60), (92, 68), (92, 76), (92, 84), (92, 92), (93, 3), (93, 11), (93, 19), (93, 27), (93, 35), (93, 43), (93, 51), (93, 59), (93, 67), (93, 75), (93, 83), (93, 91), (93, 99), (94, 2), (94, 10), (94, 18), (94, 26), (94, 34), (94, 42), (94, 50), (94, 58), (94, 66), (94, 74), (94, 82), (94, 90), (94, 98), (95, 1), (95, 9), (95, 17), (95, 25), (95, 33), (95, 41), (95, 49), (95, 57), (95, 65), (95, 73), (95, 81), (95, 89), (95, 97), (96, 0), (96, 8), (96, 16), (96, 24), (96, 32), (96, 40), (96, 48), (96, 56), (96, 64), (96, 72), (96, 80), (96, 88), (96, 96), (97, 7), (97, 15), (97, 23), (97, 31), (97, 39), (97, 47), (97, 55), (97, 63), (97, 71), (97, 79), (97, 87), (97, 95), (98, 6), (98, 14), (98, 22), (98, 30), (98, 38), (98, 46), (98, 54), (98, 62), (98, 70), (98, 78), (98, 86), (98, 94), (99, 5), (99, 13), (99, 21), (99, 29), (99, 37), (99, 45), (99, 53), (99, 61), (99, 69), (99, 77), (99, 85), (99, 93)]
>>> 