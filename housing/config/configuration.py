from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig, \
    ModelTrainerConfig,ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import  *




class Configuration:
    def __init__(self,
                 config_file_path:str=CONFIG_FILE_PATH,
                 current_time_stamp:str=CURRENT_TIME_STAMP
                 ) -> None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp
        pass
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass
    def get_data_validation_config(self) -> DataValidationConfig:
        pass
    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        pass
    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        pass
    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        pass
