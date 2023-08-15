import pytest

from src.algorithms.symmetric.aes import sub_bytes


def test_sub_bytes():
    samples = [
        {
            'initial': [
                [0x32, 0x88, 0x31, 0xe0],
                [0x43, 0x5a, 0x31, 0x37],
                [0xf6, 0x30, 0x98, 0x07],
                [0xa8, 0x8d, 0xa2, 0x34]
            ],
            'expected': [
                [0x23, 0x80, 0x7c, 0xeb],
                [0x5f, 0x59, 0x7c, 0x4d],
                [0xd7, 0x30, 0x91, 0x26],
                [0x4f, 0x5e, 0x20, 0xfa]
            ]
        },
        {
            'initial': [
                [0x00, 0x01, 0x02, 0x03],
                [0x04, 0x05, 0x06, 0x07],
                [0x08, 0x09, 0x0a, 0x0b],
                [0x0c, 0x0d, 0x0e, 0x0f]
            ],
            'expected': [
                [0x63, 0x7c, 0x77, 0x7b],
                [0xf2, 0x6b, 0x6f, 0xc5],
                [0x30, 0x01, 0x67, 0x2b],
                [0xfe, 0xd7, 0xab, 0x76]
            ]
        },
        {
            'initial': [
                [0xff, 0xee, 0xdd, 0xcc],
                [0xbb, 0xaa, 0x99, 0x88],
                [0x77, 0x66, 0x55, 0x44],
                [0x33, 0x22, 0x11, 0x00]
            ],
            'expected': [
                [0x16, 0x49, 0xd7, 0x30],
                [0xcb, 0x13, 0x53, 0x77],
                [0xf1, 0xfa, 0x34, 0x20],
                [0x0b, 0x3d, 0xe0, 0x3c]
            ]
        }
    ]

    for sample in samples:
        initial_state = sample['initial']
        expected_state = sample['expected']
        result_state = sub_bytes(initial_state)
        assert result_state == expected_state, f"Expected {expected_state}, but got {result_state}"
