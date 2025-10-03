from src.rubiks_cube_class import RubiksCube
import unittest
import tempfile
import os

class TestRubiksCube(unittest.TestCase):

    def test_1(self):
        cube = RubiksCube()
        self.assertTrue(cube.is_solved())

    def test_2(self):
        cube = RubiksCube()
        cube.apply("U")
        self.assertFalse(cube.is_solved())

    def test_3(self):
        cube = RubiksCube()
        cube.apply("U'")
        self.assertFalse(cube.is_solved())

    def test_4(self):
        cube = RubiksCube()
        cube.apply("U2")
        self.assertFalse(cube.is_solved())

    def test_5(self):
        cube = RubiksCube()
        cube.apply("R")
        self.assertFalse(cube.is_solved())

    def test_6(self):
        cube = RubiksCube()
        cube.apply("F")
        self.assertFalse(cube.is_solved())

    def test_7(self):
        cube = RubiksCube()
        cube.apply("D")
        self.assertFalse(cube.is_solved())

    def test_8(self):
        cube = RubiksCube()
        cube.apply("L")
        self.assertFalse(cube.is_solved())

    def test_9(self):
        cube = RubiksCube()
        cube.apply("B")
        self.assertFalse(cube.is_solved())

    def test_10(self):
        cube = RubiksCube()
        cube.apply("M")
        self.assertFalse(cube.is_solved())

    def test_11(self):
        cube = RubiksCube()
        cube.apply("E")
        self.assertFalse(cube.is_solved())

    def test_12(self):
        cube = RubiksCube()
        cube.apply("S")
        self.assertFalse(cube.is_solved())

    def test_13(self):
        cube = RubiksCube()
        cube.apply("U U'")
        self.assertTrue(cube.is_solved())

    def test_14(self):
        cube = RubiksCube()
        cube.apply("U2 U2")
        self.assertTrue(cube.is_solved())

    def test_15(self):
        cube = RubiksCube()
        cube.apply("R U R' U'")
        cube.apply("U R U' R'")
        self.assertTrue(cube.is_solved())

    def test_16(self):
        cube = RubiksCube()
        scramble = cube.random_scramble(10, seed=42)
        self.assertFalse(cube.is_solved())
        self.assertIsInstance(scramble, str)
        self.assertTrue(len(scramble.split()) == 10)

    def test_17(self):
        cube = RubiksCube()
        cube.apply("R U R'")

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name

        try:
            cube.save(temp_path)
            cube2 = RubiksCube()
            cube2.load(temp_path)

            for face_name in cube.faces:
                self.assertEqual(cube.faces[face_name], cube2.faces[face_name])
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_18(self):
        cube = RubiksCube()
        cube.apply("R U R' U'")
        cube.reset()
        self.assertTrue(cube.is_solved())

    def test_19(self):
        cube = RubiksCube()
        str_repr = str(cube)
        self.assertIsInstance(str_repr, str)
        self.assertGreater(len(str_repr), 0)

    def test_20(self):
        cube = RubiksCube()
        with self.assertRaises(ValueError):
            cube.apply("X")

    def test_21(self):
        cube = RubiksCube()
        cube.apply("")
        self.assertTrue(cube.is_solved())

    def test_22(self):
        cube = RubiksCube()
        cube.apply("   ")
        self.assertTrue(cube.is_solved())

    def test_23(self):
        cube = RubiksCube()
        cube.apply("R U R' U' R' F R2 U' R' U' R U R' F'")
        self.assertFalse(cube.is_solved())

    def test_24(self):
        cube = RubiksCube()
        cube.apply("U2 D2 L2 R2 F2 B2")
        cube.apply("B2 F2 R2 L2 D2 U2")
        self.assertTrue(cube.is_solved())

    def test_25(self):
        cube = RubiksCube()
        cube.apply("M M'")
        self.assertTrue(cube.is_solved())

    def test_26(self):
        cube = RubiksCube()
        cube.apply("E E'")
        self.assertTrue(cube.is_solved())


    def test_28(self):
        cube = RubiksCube()
        expected_colors = {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
            'F': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
            'B': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
            'L': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
            'R': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
        }

        for face_name, expected_face in expected_colors.items():
            self.assertEqual(cube.faces[face_name], expected_face)

    def test_29(self):
        cube = RubiksCube()

        valid_moves = ["U", "U'", "U2", "R", "R'", "R2", "M", "M'", "M2"]
        for move in valid_moves:
            try:
                cube.apply(move)
                cube.reset()
            except Exception as e:
                self.fail(f"Move {move} failed with error: {e}")

    def test_30(self):
        cube = RubiksCube()
        scramble = cube.random_scramble(20, seed=123)
        moves = scramble.split()

        for i in range(1, len(moves)):
            current_face = moves[i][0]
            prev_face = moves[i - 1][0]
            self.assertNotEqual(current_face, prev_face)

    def test_31(self):
        cube = RubiksCube()
        self.assertEqual(cube.DEFAULT_COLORS['U'], 'W')
        self.assertEqual(cube.DEFAULT_COLORS['D'], 'Y')
        self.assertEqual(cube.DEFAULT_COLORS['F'], 'G')
        self.assertEqual(cube.DEFAULT_COLORS['B'], 'B')
        self.assertEqual(cube.DEFAULT_COLORS['L'], 'O')
        self.assertEqual(cube.DEFAULT_COLORS['R'], 'R')

    def test_32(self):
        cube = RubiksCube()
        expected_order = ["U", "R", "F", "D", "L", "B"]
        self.assertEqual(cube.ORDER, expected_order)

    def test_33(self):
        cube = RubiksCube()
        test_face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        rotated_cw = cube._rot90_cw(test_face)
        expected_cw = [['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3']]
        self.assertEqual(rotated_cw, expected_cw)

    def test_34(self):
        cube = RubiksCube()
        test_face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        rotated_ccw = cube._rot90_ccw(test_face)
        expected_ccw = [['3', '6', '9'], ['2', '5', '8'], ['1', '4', '7']]
        self.assertEqual(rotated_ccw, expected_ccw)

    def test_35(self):
        cube = RubiksCube()
        test_face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        rotated_180 = cube._rot180(test_face)
        expected_180 = [['9', '8', '7'], ['6', '5', '4'], ['3', '2', '1']]
        self.assertEqual(rotated_180, expected_180)

    def test_36(self):
        cube = RubiksCube()
        test_face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        col = cube._get_col(test_face, 1)
        expected_col = ['2', '5', '8']
        self.assertEqual(col, expected_col)

    def test_37(self):
        cube = RubiksCube()
        test_face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        cube._set_col(test_face, 1, ['a', 'b', 'c'])
        expected_face = [['1', 'a', '3'], ['4', 'b', '6'], ['7', 'c', '9']]
        self.assertEqual(test_face, expected_face)

    def test_38(self):
        cube = RubiksCube()
        cube.apply("R L' U2 D' F B2")
        self.assertFalse(cube.is_solved())

    def test_39(self):
        cube = RubiksCube()
        with self.assertRaises(ValueError):
            cube.apply("InvalidMove")

    def test_40(self):
        cube = RubiksCube()
        cube.apply("")
        self.assertTrue(cube.is_solved())

    def test_41(self):
        cube = RubiksCube()
        initial_state = str(cube)
        cube.apply("R R'")
        self.assertEqual(str(cube), initial_state)

    def test_42(self):
        cube1 = RubiksCube()
        cube2 = RubiksCube()
        cube1.apply("R")
        cube2.apply("R")
        self.assertEqual(cube1.faces, cube2.faces)

    def test_43(self):
        cube = RubiksCube()
        scramble1 = cube.random_scramble(15, seed=1)
        cube.reset()
        scramble2 = cube.random_scramble(15, seed=1)
        self.assertEqual(scramble1, scramble2)


    def test_45(self):
        cube = RubiksCube()
        for move in ["U2", "D2", "L2", "R2", "F2", "B2"]:
            cube.apply(move + " " + move)
            self.assertTrue(cube.is_solved())
            cube.reset()

    def test_46(self):
        cube = RubiksCube()
        cube.apply("U")
        cube.apply("D")
        cube.apply("L")
        cube.apply("R")
        cube.apply("F")
        cube.apply("B")
        self.assertFalse(cube.is_solved())

    def test_47(self):
        cube = RubiksCube()
        with self.assertRaises(ValueError):
            cube.apply("U U2'")

    def test_48(self):
        cube = RubiksCube()
        cube.apply("M2 E2 S2")
        cube.apply("S2 E2 M2")
        self.assertTrue(cube.is_solved())

    def test_49(self):
        cube = RubiksCube()
        cube.apply("R U R' U'")
        state1 = str(cube)
        cube.reset()
        cube.apply("U R U' R'")
        state2 = str(cube)
        self.assertNotEqual(state1, state2)

    def test_50(self):
        cube = RubiksCube()
        self.assertTrue(callable(cube.turn))
        self.assertTrue(callable(cube.apply))
        self.assertTrue(callable(cube.reset))
        self.assertTrue(callable(cube.is_solved))


if __name__ == "__main__":
    unittest.main()