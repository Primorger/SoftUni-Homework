from unittest import TestCase, main
from project.star_system import StarSystem


class TestStarSystem(TestCase):

    def test_constructor(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        self.assertEqual(system.name, "star1")
        self.assertEqual(system.star_type, "Yellow dwarf")
        self.assertEqual(system.system_type, "Binary")
        self.assertEqual(system.num_planets, 3)
        self.assertEqual(system.habitable_zone_range, (0.5, 2.0))

    def test_constructor_invalid(self):
        with self.assertRaises(ValueError):
            StarSystem("", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("   ", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("star1", "Invalid", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("star1", "Yellow dwarf", "Invalid", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("star1", "Yellow dwarf", "Binary", -1, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("star1", "Yellow dwarf", "Binary", 3, (3.0, 1.0))

    def test_star_type_non_string_raises(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            system.star_type = None
        with self.assertRaises(ValueError):
            system.star_type = 123

    def test_system_type_non_string_raises(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            system.system_type = None
        with self.assertRaises(ValueError):
            system.system_type = 123

    def test_name_property(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.name = "star2"
        self.assertEqual(system.name, "star2")
        with self.assertRaises(ValueError):
            system.name = ""

    def test_star_type_property(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.star_type = "Red giant"
        self.assertEqual(system.star_type, "Red giant")
        with self.assertRaises(ValueError):
            system.star_type = "Invalid"

    def test_system_type_property(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.system_type = "Single"
        self.assertEqual(system.system_type, "Single")
        with self.assertRaises(ValueError):
            system.system_type = "Invalid"

    def test_num_planets_property(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.num_planets = 5
        self.assertEqual(system.num_planets, 5)
        with self.assertRaises(ValueError):
            system.num_planets = -1

    def test_habitable_zone_range_property(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.habitable_zone_range = (1.0, 3.0)
        self.assertEqual(system.habitable_zone_range, (1.0, 3.0))
        with self.assertRaises(ValueError):
            system.habitable_zone_range = (3.0, 1.0)

    def test_is_habitable(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        self.assertTrue(system.is_habitable)
        system.num_planets = 0
        self.assertFalse(system.is_habitable)
        system.habitable_zone_range = None
        system.num_planets = 3
        self.assertFalse(system.is_habitable)

    def test_constructor_none_habitable_zone(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 2, None)
        self.assertIsNone(system.habitable_zone_range)
        self.assertFalse(system.is_habitable)

    def test_constructor_zero_planets(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 0, (0.5, 2.0))
        self.assertEqual(system.num_planets, 0)
        self.assertFalse(system.is_habitable)

    def test_valid_star_types(self):
        for star_type in ['Red giant', 'Blue giant', 'Yellow dwarf', 'Red dwarf', 'Brown dwarf']:
            system = StarSystem("test", star_type, "Binary", 2, (0.5, 2.0))
            self.assertEqual(system.star_type, star_type)

    def test_star_type_case_sensitive(self):
        with self.assertRaises(ValueError):
            StarSystem("star1", "yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("star1", "YELLOW DWARF", "Binary", 3, (0.5, 2.0))

    def test_system_type_case_sensitive(self):
        with self.assertRaises(ValueError):
            StarSystem("star1", "Yellow dwarf", "binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            StarSystem("star1", "Yellow dwarf", "BINARY", 3, (0.5, 2.0))

    def test_name_non_string_raises(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises((AttributeError, TypeError, ValueError)):
            system.name = None
        with self.assertRaises((AttributeError, TypeError, ValueError)):
            system.name = 123

    def test_num_planets_non_int_raises(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises((TypeError, ValueError)):
            system.num_planets = "3"

    def test_habitable_zone_range_invalid_type(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises((TypeError, ValueError)):
            system.habitable_zone_range = 5

    def test_error_messages(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        try:
            system.name = ""
            self.fail("Should raise ValueError")
        except ValueError as e:
            self.assertIn("non-empty", str(e))
        
        try:
            system.num_planets = -1
            self.fail("Should raise ValueError")
        except ValueError as e:
            self.assertIn("non-negative", str(e))

    def test_multiple_property_mutations(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        for i in range(5):
            system.num_planets = i
            self.assertEqual(system.num_planets, i)
            self.assertEqual(system.name, "star1")

    def test_habitable_zone_boundary_float_precision(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.habitable_zone_range = (0.1, 0.10000001)
        self.assertEqual(system.habitable_zone_range[0], 0.1)

    def test_compare_systems_with_same_range(self):
        system1 = StarSystem("Alpha", "Yellow dwarf", "Binary", 3, (0.5, 2.5))
        system2 = StarSystem("Beta", "Red giant", "Single", 2, (1.0, 3.0))
        result = StarSystem.compare_star_systems(system1, system2)
        self.assertIn("Beta", result)

    def test_habitable_zone_valid_to_none(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        self.assertTrue(system.is_habitable)
        system.habitable_zone_range = None
        self.assertFalse(system.is_habitable)

    def test_habitable_zone_none_to_valid(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, None)
        self.assertFalse(system.is_habitable)
        system.habitable_zone_range = (0.5, 2.0)
        self.assertTrue(system.is_habitable)

    def test_habitable_zone_invalid_length(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            system.habitable_zone_range = (1.0,)
        with self.assertRaises(ValueError):
            system.habitable_zone_range = (1.0, 2.0, 3.0)

    def test_habitable_zone_negative_values(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.habitable_zone_range = (-1.0, 0.5)
        self.assertEqual(system.habitable_zone_range, (-1.0, 0.5))

    def test_gt_operator_very_close_ranges(self):
        system1 = StarSystem("system1", "Yellow dwarf", "Binary", 3, (0.5, 2.001))
        system2 = StarSystem("system2", "Red giant", "Single", 2, (0.5, 2.0))
        self.assertTrue(system1 > system2)

    def test_gt_operator_both_habitable(self):
        system1 = StarSystem("system1", "Yellow dwarf", "Binary", 1, (0.5, 2.0))
        system2 = StarSystem("system2", "Red giant", "Single", 1000, (0.5, 2.0))
        self.assertFalse(system1 > system2)

    def test_is_habitable_both_conditions_needed(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 0, None)
        self.assertFalse(system.is_habitable)

    def test_name_with_leading_trailing_spaces(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.name = " star "
        self.assertEqual(system.name, " star ")

    def test_num_planets_sequential_changes(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        system.num_planets = 10
        self.assertTrue(system.is_habitable)
        system.num_planets = 0
        self.assertFalse(system.is_habitable)
        system.num_planets = 5
        self.assertTrue(system.is_habitable)

    def test_property_changes_dont_affect_others(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        original_name = system.name
        system.star_type = "Red giant"
        self.assertEqual(system.name, original_name)
        system.num_planets = 10
        self.assertEqual(system.star_type, "Red giant")

    def test_habitable_zone_zero_width_rejected(self):
        system = StarSystem("star1", "Yellow dwarf", "Binary", 3, (0.5, 2.0))
        with self.assertRaises(ValueError):
            system.habitable_zone_range = (2.0, 2.0)

    def test_gt_operator_same_system_names(self):
        system1 = StarSystem("Same", "Yellow dwarf", "Binary", 3, (0.5, 3.0))
        system2 = StarSystem("Same", "Red giant", "Single", 2, (1.0, 2.0))
        self.assertTrue(system1 > system2)

    def test_gt_operator(self):
        system1 = StarSystem("system1", "Yellow dwarf", "Binary", 3, (0.5, 3.0))
        system2 = StarSystem("system2", "Red giant", "Single", 2, (1.0, 2.0))
        self.assertTrue(system1 > system2)
        
        system3 = StarSystem("system3", "Yellow dwarf", "Binary", 3, (0.5, 1.5))
        system4 = StarSystem("system4", "Red giant", "Single", 2, (1.0, 3.0))
        self.assertFalse(system3 > system4)
        
        system5 = StarSystem("system5", "Yellow dwarf", "Binary", 0, (0.5, 2.0))
        system6 = StarSystem("system6", "Red giant", "Single", 2, (1.0, 3.0))
        with self.assertRaises(ValueError):
            _ = system5 > system6

    def test_compare_star_systems(self):
        system1 = StarSystem("Alpha", "Yellow dwarf", "Binary", 3, (0.5, 3.0))
        system2 = StarSystem("Beta", "Red giant", "Single", 2, (1.0, 2.0))
        result = StarSystem.compare_star_systems(system1, system2)
        self.assertEqual(result, "Alpha has a wider habitable zone than Beta.")
        
        system3 = StarSystem("Alpha", "Yellow dwarf", "Binary", 3, (0.5, 1.5))
        system4 = StarSystem("Beta", "Red giant", "Single", 2, (1.0, 3.0))
        result = StarSystem.compare_star_systems(system3, system4)
        self.assertEqual(result, "Beta has a wider or equal habitable zone compared to Alpha.")
        
        system5 = StarSystem("Alpha", "Yellow dwarf", "Binary", 0, (0.5, 2.0))
        system6 = StarSystem("Beta", "Red giant", "Single", 2, (1.0, 3.0))
        result = StarSystem.compare_star_systems(system5, system6)
        self.assertIn("Comparison not possible", result)


if __name__ == "__main__":
    main()
