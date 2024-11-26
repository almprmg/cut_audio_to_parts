from pydub import AudioSegment

def split_audio(file_path, part_length_minutes):

     
        audio = AudioSegment.from_file(file_path)

        part_length_ms = part_length_minutes * 60 * 1000
        
  
        total_length_ms = len(audio)
        num_parts = (total_length_ms // part_length_ms) + (1 if total_length_ms % part_length_ms else 0)
        
     
        for i in range(num_parts):
            start_time = i * part_length_ms
            end_time = min(start_time + part_length_ms, total_length_ms)
            part = audio[start_time:end_time]
       
            output_file = f"part_{i + 1}.mp3"
            part.export(output_file, format="mp3")
            print(f"تم حفظ الجزء: {output_file}")

def convert_to_mp3(input_file, output_file):

     
        audio = AudioSegment.from_file(input_file)
        
   
        audio.export(output_file, format="mp3")
        print(f"تم تحويل الملف بنجاح إلى: {output_file}")


input_file = "..//aodue1.m4a" 
output_file = "..//aodue1.mp3" 
convert_to_mp3(input_file, output_file)

split_audio(input_file, 29)
