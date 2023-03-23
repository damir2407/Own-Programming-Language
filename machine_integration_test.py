#!/usr/bin/python3
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
# pylint: disable=missing-class-docstring
# pylint: disable=no-self-use

import unittest

import machine
import translator


def start(source_code, output_file, data_file, input_file):
    translator.main([source_code, output_file, data_file])
    if input_file == "":
        return machine.main([output_file, data_file])
    return machine.main([output_file, data_file, input_file])


class TestMachine(unittest.TestCase):

    def test_hello_world(self):
        output = start("examples/hello_world", "examples/hello_world_opcodes", "examples/data_file", "")
        self.assertEqual(output, 'Hello world!')

    def test_cat(self):
        output = start("examples/cat", "examples/cat_opcodes", "examples/data_file", "examples/hello_text")
        self.assertEqual(output, 'hello')

    def test_prob2(self):
        output = start("examples/prob2", "examples/prob2_opcodes", "examples/data_file", "")
        self.assertEqual(output, '4613732')

    def test_first(self):
        output = start("examples/test1", "examples/test1_opcodes", "examples/data_file", "")
        self.assertEqual(output, '99')

    def test_second(self):
        output = start("examples/test2", "examples/test2_opcodes", "examples/data_file", "")
        self.assertEqual(output, '-1')
