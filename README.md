# Crewai Agents with Ollama to create Storybooks (simplify testing)
- Start: 10AM _ 18 Mar 2024
- End: 03PM _ 18 Mar 2024

![alt-text](https://github.com/Mr-Jack-Tung/crewai-agents-ollama-create-storybooks/blob/main/crewai_logo.jpg)

## Lý do:
- Từ trước đến giờ cũng đã ấp ủ làm cái em bot tự động thực hiện một số công việc giúp mình, tuy nhiên 1 em thì cũng chưa đã, muốn có vài ba em "phục vụ" cơ. Muốn và ý tưởng thì là vậy nhưng thực hiện thì cũng chưa cụ thể ra làm sao nên đành tạm gác ý tưởng đó lại đã ^^
- Tối qua 17 Mar 2024, lúc sắp đi ngủ rồi, tự dưng xem Youtube thấy có anh Mervin Praison làm cái demo Create Illustrated Storybooks Instantly with Crew AI Agents! (Groq) _ https://www.youtube.com/watch?v=vWukuS48RbY , chỉ nghe cái tiêu đề thôi cũng thấy quá đã rồi, thành ra lại phải xem cho hết và tìm hiểu xem cái CrawAi Agents là gì mà nó làm hay vậy. Càng xem thì lại càng ... mất ngủ vì ... sướng ^^
- Sáng nay 18 Mar 2024, bắt tay vào làm một mạch để test cho xong cái source code demo của anh Mervin Praison, xem nó chạy local thế nào ... vậy mà nó work (at 3PM today), ngon ghê ^^ ... nó chạy roẹt một cái ra luôn thành phẩm là một file PDF truyện đọc trẻ em, mình ngắt phần tạo ảnh vì chỉ muốn làm một cái test demo thật đơn giản xem cái CrewAi Agents nó phối hợp làm việc với nhau ra sao ^^

## Ứng dụng:
- Tạo ra các Nhóm làm việc (Crew, Team) gồm nhiều Nhân sự (Agents) làm việc nhóm với nhau để hoàn thành một công việc cụ thể, có thể ứng dụng tạo ra các công ty ảo (gồm nhiều nhóm làm việc, nhân sự ảo bằng AI có các chức năng và chuyên môn khác nhau) để hoàn thành các công việc thực tế. Ví dụ như công ty phần mềm, công ty thiết kế, công ty sáng tạo nội dung, công ty quảng cáo, công ty nghiên cứu thị trường, công ty tư vấn kinh doanh, công ty đầu tư ...

![alt-text](https://github.com/Mr-Jack-Tung/crewai-agents-ollama-create-storybooks/blob/main/chat-dev-software-company-1.jpeg)

## Tham khảo:
- Create Illustrated Storybooks Instantly with Crew AI Agents! (Groq) _ https://www.youtube.com/watch?v=vWukuS48RbY
- CrewAI Groq Create Story Books _ By praison (March 17, 2024) _ https://mer.vin/2024/03/crewai-groq-create-story-books/
- AI Agents Crews are game-changing _ https://blog.langchain.dev/crewai-unleashed-future-of-ai-agent-teams/
- crewAI: Cutting-edge framework for orchestrating role-playing, autonomous AI agents _ https://github.com/joaomdmoura/crewAI

![alt-text](https://github.com/Mr-Jack-Tung/crewai-agents-ollama-create-storybooks/blob/main/crewAI-mindmap.jpg)

## Quá trình thử nghiệm:
- Cài đặt các bộ thư viện cần thiết:
  - pip install crewai
  - pip install -U 'crewai[tools]' mdpdf
  - và các bộ thư viện khác nếu hệ thống yêu cầu
- Copy source code file https://mer.vin/2024/03/crewai-groq-create-story-books/
- Cài đặt và chạy Ollama mistral
- Sửa lại source code để chạy các phần chính là gen ra câu chuyện, cắt bỏ phần tạo ảnh mô tả để giảm thiểu sự phức tạp và thời gian xử lý
- Tạo file template.md
- và .. chạy thử ~~> Ok! ~> Nhóm Agents này đã cùng phối hợp làm việc với nhau một cách ăn ý và tạo ra sản phẩm 'story.pdf'

## Kết quả thử nghiệm:
![alt-text](https://github.com/Mr-Jack-Tung/crewai-agents-ollama-create-storybooks/blob/main/crewai-agents-ollama-create-storybooks_results_Screenshot%202024-03-18_01.jpg)
