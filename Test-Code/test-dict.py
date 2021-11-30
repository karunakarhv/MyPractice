cell = {
    "16": {
        "_tab[0]prach_config_index": 4,
        "band": 30,
        "cqi_resource_count": 960,
        "delta_pucch_shift": 2,
        "dl_cyclic_prefix": "normal",
        "dl_earfcn": 9820,
        "dl_freq": 2355000000,
        "dl_qam": 256,
        "gain": 0,
        "gbr": {
            "dl_limit": 10034880,
            "ul_limit": 10195200
        },
        "mode": "FDD",
        "n_antenna_dl": 1,
        "n_antenna_ul": 1,
        "n_cs_an": 0,
        "n_id_cell": 0,
        "n_layer_dl": 1,
        "n_layer_ul": 1,
        "n_rb_cqi": 4,
        "n_rb_dl": 100,
        "n_rb_ul": 100,
        "plmn_list": [{
                "plmn": "00101",
                "reserved": False
            }, {
                "plmn": "310410",
                "reserved": False
            }
        ],
        "prach_freq_offset": 4,
        "prach_sequence_index": 50,
        "pucch_ack_nack_start": 12,
        "pucch_allocation": [{
                "n": 24,
                "rbs": 4,
                "type": "2/2a/2b"
            }
        ],
        "pucch_reserved_rbs": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "rf_port": 0,
        "sr_resource_count": 160,
        "srs_resources": {
            "freqs": 2,
            "offsets": 8,
            "total": 32
        },
        "tac": 1,
        "ul_cyclic_prefix": "normal",
        "ul_disabled": False,
        "ul_earfcn": 27710,
        "ul_freq": 2310000000,
        "ul_qam": 64
    },
    "18": {
        "_tab[0]prach_config_index": 4,
        "band": 48,
        "cqi_resource_count": 191,
        "delta_pucch_shift": 2,
        "dl_cyclic_prefix": "normal",
        "dl_earfcn": 55690,
        "dl_freq": 3595000000,
        "dl_qam": 256,
        "gain": 0,
        "gbr": {
            "dl_limit": 3714880,
            "ul_limit": 806400
        },
        "mode": "TDD",
        "n_antenna_dl": 1,
        "n_antenna_ul": 1,
        "n_cs_an": 0,
        "n_id_cell": 2,
        "n_layer_dl": 1,
        "n_layer_ul": 1,
        "n_rb_cqi": 4,
        "n_rb_dl": 50,
        "n_rb_ul": 50,
        "plmn_list": [{
                "plmn": "00101",
                "reserved": False
            }, {
                "plmn": "310410",
                "reserved": False
            }
        ],
        "prach_freq_offset": 4,
        "prach_sequence_index": 90,
        "pucch_ack_nack_start": 12,
        "pucch_allocation": [{
                "n": 24,
                "rbs": 4,
                "type": "2/2a/2b"
            }
        ],
        "pucch_reserved_rbs": [0, 0, 15, 0, 0, 0, 0, 15, 0, 0],
        "rf_port": 1,
        "sp_config": 7,
        "sr_resource_count": 31,
        "srs_resources": {
            "freqs": 2,
            "offsets": 16,
            "total": 64
        },
        "tac": 2,
        "ul_cyclic_prefix": "normal",
        "ul_disabled": False,
        "ul_earfcn": 55690,
        "ul_freq": 3595000000,
        "ul_qam": 64,
        "uldl_config": 2
    }
}

print(sum(value['band'] == 48 for value in cell.values()))

