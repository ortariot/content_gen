from imageprocessor.imageprocessor import ImageProcessor


class Classifier:
    def __init__(
        self,
        processors: list[ImageProcessor] = None,
    ):

        self.processors = processors if processors else []

    def add_processor(self, processor: ImageProcessor) -> None:
        self.processors.append(processor)

    def get_classification(
        self,
        object_path: str,
    ):

        classification = {}
        for proc in self.processors:
            result = proc.execute(object_path)

            for avg, file_name in result:
                if file_name in classification:
                    classification[file_name] += avg
                else:
                    classification[file_name] = avg

        sorted(classification, key=lambda x: x[1])

        return classification
