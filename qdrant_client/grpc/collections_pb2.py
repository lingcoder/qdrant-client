# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collections.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63ollections.proto\x12\x06qdrant\"\xfa\x01\n\x0cVectorParams\x12\x0c\n\x04size\x18\x01 \x01(\x04\x12\"\n\x08\x64istance\x18\x02 \x01(\x0e\x32\x10.qdrant.Distance\x12\x30\n\x0bhnsw_config\x18\x03 \x01(\x0b\x32\x16.qdrant.HnswConfigDiffH\x00\x88\x01\x01\x12<\n\x13quantization_config\x18\x04 \x01(\x0b\x32\x1a.qdrant.QuantizationConfigH\x01\x88\x01\x01\x12\x14\n\x07on_disk\x18\x05 \x01(\x08H\x02\x88\x01\x01\x42\x0e\n\x0c_hnsw_configB\x16\n\x14_quantization_configB\n\n\x08_on_disk\"\xd0\x01\n\x10VectorParamsDiff\x12\x30\n\x0bhnsw_config\x18\x01 \x01(\x0b\x32\x16.qdrant.HnswConfigDiffH\x00\x88\x01\x01\x12@\n\x13quantization_config\x18\x02 \x01(\x0b\x32\x1e.qdrant.QuantizationConfigDiffH\x01\x88\x01\x01\x12\x14\n\x07on_disk\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\x0e\n\x0c_hnsw_configB\x16\n\x14_quantization_configB\n\n\x08_on_disk\"\x82\x01\n\x0fVectorParamsMap\x12-\n\x03map\x18\x01 \x03(\x0b\x32 .qdrant.VectorParamsMap.MapEntry\x1a@\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.qdrant.VectorParams:\x02\x38\x01\"\x8e\x01\n\x13VectorParamsDiffMap\x12\x31\n\x03map\x18\x01 \x03(\x0b\x32$.qdrant.VectorParamsDiffMap.MapEntry\x1a\x44\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.qdrant.VectorParamsDiff:\x02\x38\x01\"p\n\rVectorsConfig\x12&\n\x06params\x18\x01 \x01(\x0b\x32\x14.qdrant.VectorParamsH\x00\x12-\n\nparams_map\x18\x02 \x01(\x0b\x32\x17.qdrant.VectorParamsMapH\x00\x42\x08\n\x06\x63onfig\"|\n\x11VectorsConfigDiff\x12*\n\x06params\x18\x01 \x01(\x0b\x32\x18.qdrant.VectorParamsDiffH\x00\x12\x31\n\nparams_map\x18\x02 \x01(\x0b\x32\x1b.qdrant.VectorParamsDiffMapH\x00\x42\x08\n\x06\x63onfig\"3\n\x18GetCollectionInfoRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"\x18\n\x16ListCollectionsRequest\"%\n\x15\x43ollectionDescription\x12\x0c\n\x04name\x18\x01 \x01(\t\"Q\n\x19GetCollectionInfoResponse\x12&\n\x06result\x18\x01 \x01(\x0b\x32\x16.qdrant.CollectionInfo\x12\x0c\n\x04time\x18\x02 \x01(\x01\"[\n\x17ListCollectionsResponse\x12\x32\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\x1d.qdrant.CollectionDescription\x12\x0c\n\x04time\x18\x02 \x01(\x01\",\n\x0fOptimizerStatus\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x90\x02\n\x0eHnswConfigDiff\x12\x0e\n\x01m\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x19\n\x0c\x65\x66_construct\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12 \n\x13\x66ull_scan_threshold\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12!\n\x14max_indexing_threads\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x14\n\x07on_disk\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x16\n\tpayload_m\x18\x06 \x01(\x04H\x05\x88\x01\x01\x42\x04\n\x02_mB\x0f\n\r_ef_constructB\x16\n\x14_full_scan_thresholdB\x17\n\x15_max_indexing_threadsB\n\n\x08_on_diskB\x0c\n\n_payload_m\"y\n\rWalConfigDiff\x12\x1c\n\x0fwal_capacity_mb\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x1f\n\x12wal_segments_ahead\x18\x02 \x01(\x04H\x01\x88\x01\x01\x42\x12\n\x10_wal_capacity_mbB\x15\n\x13_wal_segments_ahead\"\xec\x03\n\x14OptimizersConfigDiff\x12\x1e\n\x11\x64\x65leted_threshold\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12%\n\x18vacuum_min_vector_number\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12#\n\x16\x64\x65\x66\x61ult_segment_number\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x1d\n\x10max_segment_size\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x1d\n\x10memmap_threshold\x18\x05 \x01(\x04H\x04\x88\x01\x01\x12\x1f\n\x12indexing_threshold\x18\x06 \x01(\x04H\x05\x88\x01\x01\x12\x1f\n\x12\x66lush_interval_sec\x18\x07 \x01(\x04H\x06\x88\x01\x01\x12%\n\x18max_optimization_threads\x18\x08 \x01(\x04H\x07\x88\x01\x01\x42\x14\n\x12_deleted_thresholdB\x1b\n\x19_vacuum_min_vector_numberB\x19\n\x17_default_segment_numberB\x13\n\x11_max_segment_sizeB\x13\n\x11_memmap_thresholdB\x15\n\x13_indexing_thresholdB\x15\n\x13_flush_interval_secB\x1b\n\x19_max_optimization_threads\"\x88\x01\n\x12ScalarQuantization\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.qdrant.QuantizationType\x12\x15\n\x08quantile\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x17\n\nalways_ram\x18\x03 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_quantileB\r\n\x0b_always_ram\"l\n\x13ProductQuantization\x12-\n\x0b\x63ompression\x18\x01 \x01(\x0e\x32\x18.qdrant.CompressionRatio\x12\x17\n\nalways_ram\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\r\n\x0b_always_ram\"<\n\x12\x42inaryQuantization\x12\x17\n\nalways_ram\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\r\n\x0b_always_ram\"\xb0\x01\n\x12QuantizationConfig\x12,\n\x06scalar\x18\x01 \x01(\x0b\x32\x1a.qdrant.ScalarQuantizationH\x00\x12.\n\x07product\x18\x02 \x01(\x0b\x32\x1b.qdrant.ProductQuantizationH\x00\x12,\n\x06\x62inary\x18\x03 \x01(\x0b\x32\x1a.qdrant.BinaryQuantizationH\x00\x42\x0e\n\x0cquantization\"\n\n\x08\x44isabled\"\xda\x01\n\x16QuantizationConfigDiff\x12,\n\x06scalar\x18\x01 \x01(\x0b\x32\x1a.qdrant.ScalarQuantizationH\x00\x12.\n\x07product\x18\x02 \x01(\x0b\x32\x1b.qdrant.ProductQuantizationH\x00\x12$\n\x08\x64isabled\x18\x03 \x01(\x0b\x32\x10.qdrant.DisabledH\x00\x12,\n\x06\x62inary\x18\x04 \x01(\x0b\x32\x1a.qdrant.BinaryQuantizationH\x00\x42\x0e\n\x0cquantization\"\xab\x06\n\x10\x43reateCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x30\n\x0bhnsw_config\x18\x04 \x01(\x0b\x32\x16.qdrant.HnswConfigDiffH\x00\x88\x01\x01\x12.\n\nwal_config\x18\x05 \x01(\x0b\x32\x15.qdrant.WalConfigDiffH\x01\x88\x01\x01\x12<\n\x11optimizers_config\x18\x06 \x01(\x0b\x32\x1c.qdrant.OptimizersConfigDiffH\x02\x88\x01\x01\x12\x19\n\x0cshard_number\x18\x07 \x01(\rH\x03\x88\x01\x01\x12\x1c\n\x0fon_disk_payload\x18\x08 \x01(\x08H\x04\x88\x01\x01\x12\x14\n\x07timeout\x18\t \x01(\x04H\x05\x88\x01\x01\x12\x32\n\x0evectors_config\x18\n \x01(\x0b\x32\x15.qdrant.VectorsConfigH\x06\x88\x01\x01\x12\x1f\n\x12replication_factor\x18\x0b \x01(\rH\x07\x88\x01\x01\x12%\n\x18write_consistency_factor\x18\x0c \x01(\rH\x08\x88\x01\x01\x12!\n\x14init_from_collection\x18\r \x01(\tH\t\x88\x01\x01\x12<\n\x13quantization_config\x18\x0e \x01(\x0b\x32\x1a.qdrant.QuantizationConfigH\n\x88\x01\x01\x12\x34\n\x0fsharding_method\x18\x0f \x01(\x0e\x32\x16.qdrant.ShardingMethodH\x0b\x88\x01\x01\x42\x0e\n\x0c_hnsw_configB\r\n\x0b_wal_configB\x14\n\x12_optimizers_configB\x0f\n\r_shard_numberB\x12\n\x10_on_disk_payloadB\n\n\x08_timeoutB\x11\n\x0f_vectors_configB\x15\n\x13_replication_factorB\x1b\n\x19_write_consistency_factorB\x17\n\x15_init_from_collectionB\x16\n\x14_quantization_configB\x12\n\x10_sharding_methodJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"\xc6\x03\n\x10UpdateCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12<\n\x11optimizers_config\x18\x02 \x01(\x0b\x32\x1c.qdrant.OptimizersConfigDiffH\x00\x88\x01\x01\x12\x14\n\x07timeout\x18\x03 \x01(\x04H\x01\x88\x01\x01\x12\x31\n\x06params\x18\x04 \x01(\x0b\x32\x1c.qdrant.CollectionParamsDiffH\x02\x88\x01\x01\x12\x30\n\x0bhnsw_config\x18\x05 \x01(\x0b\x32\x16.qdrant.HnswConfigDiffH\x03\x88\x01\x01\x12\x36\n\x0evectors_config\x18\x06 \x01(\x0b\x32\x19.qdrant.VectorsConfigDiffH\x04\x88\x01\x01\x12@\n\x13quantization_config\x18\x07 \x01(\x0b\x32\x1e.qdrant.QuantizationConfigDiffH\x05\x88\x01\x01\x42\x14\n\x12_optimizers_configB\n\n\x08_timeoutB\t\n\x07_paramsB\x0e\n\x0c_hnsw_configB\x11\n\x0f_vectors_configB\x16\n\x14_quantization_config\"M\n\x10\x44\x65leteCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x14\n\x07timeout\x18\x02 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_timeout\";\n\x1b\x43ollectionOperationResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04time\x18\x02 \x01(\x01\"\x94\x03\n\x10\x43ollectionParams\x12\x14\n\x0cshard_number\x18\x03 \x01(\r\x12\x17\n\x0fon_disk_payload\x18\x04 \x01(\x08\x12\x32\n\x0evectors_config\x18\x05 \x01(\x0b\x32\x15.qdrant.VectorsConfigH\x00\x88\x01\x01\x12\x1f\n\x12replication_factor\x18\x06 \x01(\rH\x01\x88\x01\x01\x12%\n\x18write_consistency_factor\x18\x07 \x01(\rH\x02\x88\x01\x01\x12 \n\x13read_fan_out_factor\x18\x08 \x01(\rH\x03\x88\x01\x01\x12\x34\n\x0fsharding_method\x18\t \x01(\x0e\x32\x16.qdrant.ShardingMethodH\x04\x88\x01\x01\x42\x11\n\x0f_vectors_configB\x15\n\x13_replication_factorB\x1b\n\x19_write_consistency_factorB\x16\n\x14_read_fan_out_factorB\x12\n\x10_sharding_methodJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\xfe\x01\n\x14\x43ollectionParamsDiff\x12\x1f\n\x12replication_factor\x18\x01 \x01(\rH\x00\x88\x01\x01\x12%\n\x18write_consistency_factor\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x1c\n\x0fon_disk_payload\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12 \n\x13read_fan_out_factor\x18\x04 \x01(\rH\x03\x88\x01\x01\x42\x15\n\x13_replication_factorB\x1b\n\x19_write_consistency_factorB\x12\n\x10_on_disk_payloadB\x16\n\x14_read_fan_out_factor\"\xa2\x02\n\x10\x43ollectionConfig\x12(\n\x06params\x18\x01 \x01(\x0b\x32\x18.qdrant.CollectionParams\x12+\n\x0bhnsw_config\x18\x02 \x01(\x0b\x32\x16.qdrant.HnswConfigDiff\x12\x36\n\x10optimizer_config\x18\x03 \x01(\x0b\x32\x1c.qdrant.OptimizersConfigDiff\x12)\n\nwal_config\x18\x04 \x01(\x0b\x32\x15.qdrant.WalConfigDiff\x12<\n\x13quantization_config\x18\x05 \x01(\x0b\x32\x1a.qdrant.QuantizationConfigH\x00\x88\x01\x01\x42\x16\n\x14_quantization_config\"\xbd\x01\n\x0fTextIndexParams\x12(\n\ttokenizer\x18\x01 \x01(\x0e\x32\x15.qdrant.TokenizerType\x12\x16\n\tlowercase\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x1a\n\rmin_token_len\x18\x03 \x01(\x04H\x01\x88\x01\x01\x12\x1a\n\rmax_token_len\x18\x04 \x01(\x04H\x02\x88\x01\x01\x42\x0c\n\n_lowercaseB\x10\n\x0e_min_token_lenB\x10\n\x0e_max_token_len\"Z\n\x12PayloadIndexParams\x12\x34\n\x11text_index_params\x18\x01 \x01(\x0b\x32\x17.qdrant.TextIndexParamsH\x00\x42\x0e\n\x0cindex_params\"\x9d\x01\n\x11PayloadSchemaInfo\x12,\n\tdata_type\x18\x01 \x01(\x0e\x32\x19.qdrant.PayloadSchemaType\x12/\n\x06params\x18\x02 \x01(\x0b\x32\x1a.qdrant.PayloadIndexParamsH\x00\x88\x01\x01\x12\x13\n\x06points\x18\x03 \x01(\x04H\x01\x88\x01\x01\x42\t\n\x07_paramsB\t\n\x07_points\"\xba\x03\n\x0e\x43ollectionInfo\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.qdrant.CollectionStatus\x12\x31\n\x10optimizer_status\x18\x02 \x01(\x0b\x32\x17.qdrant.OptimizerStatus\x12\x15\n\rvectors_count\x18\x03 \x01(\x04\x12\x16\n\x0esegments_count\x18\x04 \x01(\x04\x12(\n\x06\x63onfig\x18\x07 \x01(\x0b\x32\x18.qdrant.CollectionConfig\x12\x41\n\x0epayload_schema\x18\x08 \x03(\x0b\x32).qdrant.CollectionInfo.PayloadSchemaEntry\x12\x14\n\x0cpoints_count\x18\t \x01(\x04\x12\"\n\x15indexed_vectors_count\x18\n \x01(\x04H\x00\x88\x01\x01\x1aO\n\x12PayloadSchemaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.qdrant.PayloadSchemaInfo:\x02\x38\x01\x42\x18\n\x16_indexed_vectors_countJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\"[\n\rChangeAliases\x12(\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x17.qdrant.AliasOperations\x12\x14\n\x07timeout\x18\x02 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_timeout\"\xa2\x01\n\x0f\x41liasOperations\x12+\n\x0c\x63reate_alias\x18\x01 \x01(\x0b\x32\x13.qdrant.CreateAliasH\x00\x12+\n\x0crename_alias\x18\x02 \x01(\x0b\x32\x13.qdrant.RenameAliasH\x00\x12+\n\x0c\x64\x65lete_alias\x18\x03 \x01(\x0b\x32\x13.qdrant.DeleteAliasH\x00\x42\x08\n\x06\x61\x63tion\":\n\x0b\x43reateAlias\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x12\n\nalias_name\x18\x02 \x01(\t\"=\n\x0bRenameAlias\x12\x16\n\x0eold_alias_name\x18\x01 \x01(\t\x12\x16\n\x0enew_alias_name\x18\x02 \x01(\t\"!\n\x0b\x44\x65leteAlias\x12\x12\n\nalias_name\x18\x01 \x01(\t\"\x14\n\x12ListAliasesRequest\"7\n\x1cListCollectionAliasesRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"?\n\x10\x41liasDescription\x12\x12\n\nalias_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x02 \x01(\t\"N\n\x13ListAliasesResponse\x12)\n\x07\x61liases\x18\x01 \x03(\x0b\x32\x18.qdrant.AliasDescription\x12\x0c\n\x04time\x18\x02 \x01(\x01\"7\n\x1c\x43ollectionClusterInfoRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"6\n\x08ShardKey\x12\x11\n\x07keyword\x18\x01 \x01(\tH\x00\x12\x10\n\x06number\x18\x02 \x01(\x04H\x00\x42\x05\n\x03key\"\x95\x01\n\x0eLocalShardInfo\x12\x10\n\x08shard_id\x18\x01 \x01(\r\x12\x14\n\x0cpoints_count\x18\x02 \x01(\x04\x12#\n\x05state\x18\x03 \x01(\x0e\x32\x14.qdrant.ReplicaState\x12(\n\tshard_key\x18\x04 \x01(\x0b\x32\x10.qdrant.ShardKeyH\x00\x88\x01\x01\x42\x0c\n\n_shard_key\"\x91\x01\n\x0fRemoteShardInfo\x12\x10\n\x08shard_id\x18\x01 \x01(\r\x12\x0f\n\x07peer_id\x18\x02 \x01(\x04\x12#\n\x05state\x18\x03 \x01(\x0e\x32\x14.qdrant.ReplicaState\x12(\n\tshard_key\x18\x04 \x01(\x0b\x32\x10.qdrant.ShardKeyH\x00\x88\x01\x01\x42\x0c\n\n_shard_key\"M\n\x11ShardTransferInfo\x12\x10\n\x08shard_id\x18\x01 \x01(\r\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x04\x12\n\n\x02to\x18\x03 \x01(\x04\x12\x0c\n\x04sync\x18\x04 \x01(\x08\"\xd7\x01\n\x1d\x43ollectionClusterInfoResponse\x12\x0f\n\x07peer_id\x18\x01 \x01(\x04\x12\x13\n\x0bshard_count\x18\x02 \x01(\x04\x12,\n\x0clocal_shards\x18\x03 \x03(\x0b\x32\x16.qdrant.LocalShardInfo\x12.\n\rremote_shards\x18\x04 \x03(\x0b\x32\x17.qdrant.RemoteShardInfo\x12\x32\n\x0fshard_transfers\x18\x05 \x03(\x0b\x32\x19.qdrant.ShardTransferInfo\"\x84\x01\n\tMoveShard\x12\x10\n\x08shard_id\x18\x01 \x01(\r\x12\x14\n\x0c\x66rom_peer_id\x18\x02 \x01(\x04\x12\x12\n\nto_peer_id\x18\x03 \x01(\x04\x12\x30\n\x06method\x18\x04 \x01(\x0e\x32\x1b.qdrant.ShardTransferMethodH\x00\x88\x01\x01\x42\t\n\x07_method\",\n\x07Replica\x12\x10\n\x08shard_id\x18\x01 \x01(\r\x12\x0f\n\x07peer_id\x18\x02 \x01(\x04\"\xae\x01\n\x0e\x43reateShardKey\x12#\n\tshard_key\x18\x01 \x01(\x0b\x32\x10.qdrant.ShardKey\x12\x1a\n\rshards_number\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x1f\n\x12replication_factor\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x11\n\tplacement\x18\x04 \x03(\x04\x42\x10\n\x0e_shards_numberB\x15\n\x13_replication_factor\"5\n\x0e\x44\x65leteShardKey\x12#\n\tshard_key\x18\x01 \x01(\x0b\x32\x10.qdrant.ShardKey\"\x82\x03\n#UpdateCollectionClusterSetupRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\'\n\nmove_shard\x18\x02 \x01(\x0b\x32\x11.qdrant.MoveShardH\x00\x12,\n\x0freplicate_shard\x18\x03 \x01(\x0b\x32\x11.qdrant.MoveShardH\x00\x12+\n\x0e\x61\x62ort_transfer\x18\x04 \x01(\x0b\x32\x11.qdrant.MoveShardH\x00\x12\'\n\x0c\x64rop_replica\x18\x05 \x01(\x0b\x32\x0f.qdrant.ReplicaH\x00\x12\x32\n\x10\x63reate_shard_key\x18\x07 \x01(\x0b\x32\x16.qdrant.CreateShardKeyH\x00\x12\x32\n\x10\x64\x65lete_shard_key\x18\x08 \x01(\x0b\x32\x16.qdrant.DeleteShardKeyH\x00\x12\x14\n\x07timeout\x18\x06 \x01(\x04H\x01\x88\x01\x01\x42\x0b\n\toperationB\n\n\x08_timeout\"6\n$UpdateCollectionClusterSetupResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"{\n\x15\x43reateShardKeyRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\'\n\x07request\x18\x02 \x01(\x0b\x32\x16.qdrant.CreateShardKey\x12\x14\n\x07timeout\x18\x03 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_timeout\"{\n\x15\x44\x65leteShardKeyRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\'\n\x07request\x18\x02 \x01(\x0b\x32\x16.qdrant.DeleteShardKey\x12\x14\n\x07timeout\x18\x03 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_timeout\"(\n\x16\x43reateShardKeyResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"(\n\x16\x44\x65leteShardKeyResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08*@\n\x08\x44istance\x12\x13\n\x0fUnknownDistance\x10\x00\x12\n\n\x06\x43osine\x10\x01\x12\n\n\x06\x45uclid\x10\x02\x12\x07\n\x03\x44ot\x10\x03*O\n\x10\x43ollectionStatus\x12\x1b\n\x17UnknownCollectionStatus\x10\x00\x12\t\n\x05Green\x10\x01\x12\n\n\x06Yellow\x10\x02\x12\x07\n\x03Red\x10\x03*f\n\x11PayloadSchemaType\x12\x0f\n\x0bUnknownType\x10\x00\x12\x0b\n\x07Keyword\x10\x01\x12\x0b\n\x07Integer\x10\x02\x12\t\n\x05\x46loat\x10\x03\x12\x07\n\x03Geo\x10\x04\x12\x08\n\x04Text\x10\x05\x12\x08\n\x04\x42ool\x10\x06*5\n\x10QuantizationType\x12\x17\n\x13UnknownQuantization\x10\x00\x12\x08\n\x04Int8\x10\x01*=\n\x10\x43ompressionRatio\x12\x06\n\x02x4\x10\x00\x12\x06\n\x02x8\x10\x01\x12\x07\n\x03x16\x10\x02\x12\x07\n\x03x32\x10\x03\x12\x07\n\x03x64\x10\x04*&\n\x0eShardingMethod\x12\x08\n\x04\x41uto\x10\x00\x12\n\n\x06\x43ustom\x10\x01*T\n\rTokenizerType\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06Prefix\x10\x01\x12\x0e\n\nWhitespace\x10\x02\x12\x08\n\x04Word\x10\x03\x12\x10\n\x0cMultilingual\x10\x04*f\n\x0cReplicaState\x12\n\n\x06\x41\x63tive\x10\x00\x12\x08\n\x04\x44\x65\x61\x64\x10\x01\x12\x0b\n\x07Partial\x10\x02\x12\x10\n\x0cInitializing\x10\x03\x12\x0c\n\x08Listener\x10\x04\x12\x13\n\x0fPartialSnapshot\x10\x05*6\n\x13ShardTransferMethod\x12\x11\n\rStreamRecords\x10\x00\x12\x0c\n\x08Snapshot\x10\x01\x42\x15\xaa\x02\x12Qdrant.Client.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'collections_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022Qdrant.Client.Grpc'
  _VECTORPARAMSMAP_MAPENTRY._options = None
  _VECTORPARAMSMAP_MAPENTRY._serialized_options = b'8\001'
  _VECTORPARAMSDIFFMAP_MAPENTRY._options = None
  _VECTORPARAMSDIFFMAP_MAPENTRY._serialized_options = b'8\001'
  _COLLECTIONINFO_PAYLOADSCHEMAENTRY._options = None
  _COLLECTIONINFO_PAYLOADSCHEMAENTRY._serialized_options = b'8\001'
  _globals['_DISTANCE']._serialized_start=8766
  _globals['_DISTANCE']._serialized_end=8830
  _globals['_COLLECTIONSTATUS']._serialized_start=8832
  _globals['_COLLECTIONSTATUS']._serialized_end=8911
  _globals['_PAYLOADSCHEMATYPE']._serialized_start=8913
  _globals['_PAYLOADSCHEMATYPE']._serialized_end=9015
  _globals['_QUANTIZATIONTYPE']._serialized_start=9017
  _globals['_QUANTIZATIONTYPE']._serialized_end=9070
  _globals['_COMPRESSIONRATIO']._serialized_start=9072
  _globals['_COMPRESSIONRATIO']._serialized_end=9133
  _globals['_SHARDINGMETHOD']._serialized_start=9135
  _globals['_SHARDINGMETHOD']._serialized_end=9173
  _globals['_TOKENIZERTYPE']._serialized_start=9175
  _globals['_TOKENIZERTYPE']._serialized_end=9259
  _globals['_REPLICASTATE']._serialized_start=9261
  _globals['_REPLICASTATE']._serialized_end=9363
  _globals['_SHARDTRANSFERMETHOD']._serialized_start=9365
  _globals['_SHARDTRANSFERMETHOD']._serialized_end=9419
  _globals['_VECTORPARAMS']._serialized_start=30
  _globals['_VECTORPARAMS']._serialized_end=280
  _globals['_VECTORPARAMSDIFF']._serialized_start=283
  _globals['_VECTORPARAMSDIFF']._serialized_end=491
  _globals['_VECTORPARAMSMAP']._serialized_start=494
  _globals['_VECTORPARAMSMAP']._serialized_end=624
  _globals['_VECTORPARAMSMAP_MAPENTRY']._serialized_start=560
  _globals['_VECTORPARAMSMAP_MAPENTRY']._serialized_end=624
  _globals['_VECTORPARAMSDIFFMAP']._serialized_start=627
  _globals['_VECTORPARAMSDIFFMAP']._serialized_end=769
  _globals['_VECTORPARAMSDIFFMAP_MAPENTRY']._serialized_start=701
  _globals['_VECTORPARAMSDIFFMAP_MAPENTRY']._serialized_end=769
  _globals['_VECTORSCONFIG']._serialized_start=771
  _globals['_VECTORSCONFIG']._serialized_end=883
  _globals['_VECTORSCONFIGDIFF']._serialized_start=885
  _globals['_VECTORSCONFIGDIFF']._serialized_end=1009
  _globals['_GETCOLLECTIONINFOREQUEST']._serialized_start=1011
  _globals['_GETCOLLECTIONINFOREQUEST']._serialized_end=1062
  _globals['_LISTCOLLECTIONSREQUEST']._serialized_start=1064
  _globals['_LISTCOLLECTIONSREQUEST']._serialized_end=1088
  _globals['_COLLECTIONDESCRIPTION']._serialized_start=1090
  _globals['_COLLECTIONDESCRIPTION']._serialized_end=1127
  _globals['_GETCOLLECTIONINFORESPONSE']._serialized_start=1129
  _globals['_GETCOLLECTIONINFORESPONSE']._serialized_end=1210
  _globals['_LISTCOLLECTIONSRESPONSE']._serialized_start=1212
  _globals['_LISTCOLLECTIONSRESPONSE']._serialized_end=1303
  _globals['_OPTIMIZERSTATUS']._serialized_start=1305
  _globals['_OPTIMIZERSTATUS']._serialized_end=1349
  _globals['_HNSWCONFIGDIFF']._serialized_start=1352
  _globals['_HNSWCONFIGDIFF']._serialized_end=1624
  _globals['_WALCONFIGDIFF']._serialized_start=1626
  _globals['_WALCONFIGDIFF']._serialized_end=1747
  _globals['_OPTIMIZERSCONFIGDIFF']._serialized_start=1750
  _globals['_OPTIMIZERSCONFIGDIFF']._serialized_end=2242
  _globals['_SCALARQUANTIZATION']._serialized_start=2245
  _globals['_SCALARQUANTIZATION']._serialized_end=2381
  _globals['_PRODUCTQUANTIZATION']._serialized_start=2383
  _globals['_PRODUCTQUANTIZATION']._serialized_end=2491
  _globals['_BINARYQUANTIZATION']._serialized_start=2493
  _globals['_BINARYQUANTIZATION']._serialized_end=2553
  _globals['_QUANTIZATIONCONFIG']._serialized_start=2556
  _globals['_QUANTIZATIONCONFIG']._serialized_end=2732
  _globals['_DISABLED']._serialized_start=2734
  _globals['_DISABLED']._serialized_end=2744
  _globals['_QUANTIZATIONCONFIGDIFF']._serialized_start=2747
  _globals['_QUANTIZATIONCONFIGDIFF']._serialized_end=2965
  _globals['_CREATECOLLECTION']._serialized_start=2968
  _globals['_CREATECOLLECTION']._serialized_end=3779
  _globals['_UPDATECOLLECTION']._serialized_start=3782
  _globals['_UPDATECOLLECTION']._serialized_end=4236
  _globals['_DELETECOLLECTION']._serialized_start=4238
  _globals['_DELETECOLLECTION']._serialized_end=4315
  _globals['_COLLECTIONOPERATIONRESPONSE']._serialized_start=4317
  _globals['_COLLECTIONOPERATIONRESPONSE']._serialized_end=4376
  _globals['_COLLECTIONPARAMS']._serialized_start=4379
  _globals['_COLLECTIONPARAMS']._serialized_end=4783
  _globals['_COLLECTIONPARAMSDIFF']._serialized_start=4786
  _globals['_COLLECTIONPARAMSDIFF']._serialized_end=5040
  _globals['_COLLECTIONCONFIG']._serialized_start=5043
  _globals['_COLLECTIONCONFIG']._serialized_end=5333
  _globals['_TEXTINDEXPARAMS']._serialized_start=5336
  _globals['_TEXTINDEXPARAMS']._serialized_end=5525
  _globals['_PAYLOADINDEXPARAMS']._serialized_start=5527
  _globals['_PAYLOADINDEXPARAMS']._serialized_end=5617
  _globals['_PAYLOADSCHEMAINFO']._serialized_start=5620
  _globals['_PAYLOADSCHEMAINFO']._serialized_end=5777
  _globals['_COLLECTIONINFO']._serialized_start=5780
  _globals['_COLLECTIONINFO']._serialized_end=6222
  _globals['_COLLECTIONINFO_PAYLOADSCHEMAENTRY']._serialized_start=6105
  _globals['_COLLECTIONINFO_PAYLOADSCHEMAENTRY']._serialized_end=6184
  _globals['_CHANGEALIASES']._serialized_start=6224
  _globals['_CHANGEALIASES']._serialized_end=6315
  _globals['_ALIASOPERATIONS']._serialized_start=6318
  _globals['_ALIASOPERATIONS']._serialized_end=6480
  _globals['_CREATEALIAS']._serialized_start=6482
  _globals['_CREATEALIAS']._serialized_end=6540
  _globals['_RENAMEALIAS']._serialized_start=6542
  _globals['_RENAMEALIAS']._serialized_end=6603
  _globals['_DELETEALIAS']._serialized_start=6605
  _globals['_DELETEALIAS']._serialized_end=6638
  _globals['_LISTALIASESREQUEST']._serialized_start=6640
  _globals['_LISTALIASESREQUEST']._serialized_end=6660
  _globals['_LISTCOLLECTIONALIASESREQUEST']._serialized_start=6662
  _globals['_LISTCOLLECTIONALIASESREQUEST']._serialized_end=6717
  _globals['_ALIASDESCRIPTION']._serialized_start=6719
  _globals['_ALIASDESCRIPTION']._serialized_end=6782
  _globals['_LISTALIASESRESPONSE']._serialized_start=6784
  _globals['_LISTALIASESRESPONSE']._serialized_end=6862
  _globals['_COLLECTIONCLUSTERINFOREQUEST']._serialized_start=6864
  _globals['_COLLECTIONCLUSTERINFOREQUEST']._serialized_end=6919
  _globals['_SHARDKEY']._serialized_start=6921
  _globals['_SHARDKEY']._serialized_end=6975
  _globals['_LOCALSHARDINFO']._serialized_start=6978
  _globals['_LOCALSHARDINFO']._serialized_end=7127
  _globals['_REMOTESHARDINFO']._serialized_start=7130
  _globals['_REMOTESHARDINFO']._serialized_end=7275
  _globals['_SHARDTRANSFERINFO']._serialized_start=7277
  _globals['_SHARDTRANSFERINFO']._serialized_end=7354
  _globals['_COLLECTIONCLUSTERINFORESPONSE']._serialized_start=7357
  _globals['_COLLECTIONCLUSTERINFORESPONSE']._serialized_end=7572
  _globals['_MOVESHARD']._serialized_start=7575
  _globals['_MOVESHARD']._serialized_end=7707
  _globals['_REPLICA']._serialized_start=7709
  _globals['_REPLICA']._serialized_end=7753
  _globals['_CREATESHARDKEY']._serialized_start=7756
  _globals['_CREATESHARDKEY']._serialized_end=7930
  _globals['_DELETESHARDKEY']._serialized_start=7932
  _globals['_DELETESHARDKEY']._serialized_end=7985
  _globals['_UPDATECOLLECTIONCLUSTERSETUPREQUEST']._serialized_start=7988
  _globals['_UPDATECOLLECTIONCLUSTERSETUPREQUEST']._serialized_end=8374
  _globals['_UPDATECOLLECTIONCLUSTERSETUPRESPONSE']._serialized_start=8376
  _globals['_UPDATECOLLECTIONCLUSTERSETUPRESPONSE']._serialized_end=8430
  _globals['_CREATESHARDKEYREQUEST']._serialized_start=8432
  _globals['_CREATESHARDKEYREQUEST']._serialized_end=8555
  _globals['_DELETESHARDKEYREQUEST']._serialized_start=8557
  _globals['_DELETESHARDKEYREQUEST']._serialized_end=8680
  _globals['_CREATESHARDKEYRESPONSE']._serialized_start=8682
  _globals['_CREATESHARDKEYRESPONSE']._serialized_end=8722
  _globals['_DELETESHARDKEYRESPONSE']._serialized_start=8724
  _globals['_DELETESHARDKEYRESPONSE']._serialized_end=8764
# @@protoc_insertion_point(module_scope)
