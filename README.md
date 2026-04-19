# Sentiment Analysis API

A production-ready sentiment analysis API built with FastAPI and HuggingFace Transformers.

## What it does
Analyzes English text and returns whether the sentiment is POSITIVE or NEGATIVE with a confidence score between 0 and 1.

## Tech Stack
- **FastAPI** — High-performance Python web framework for building APIs
- **HuggingFace Transformers** — DistilBERT model fine-tuned on SST-2 dataset
- **Prometheus** — Metrics collection and monitoring
- **Grafana** — Metrics visualization and dashboards
- **Docker** — Containerization for consistent deployment

## Project Structure

```
01-sentiment-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /predict | Analyze sentiment |
| GET | /metrics | Prometheus metrics |

## Example

Request:
```
POST /predict?text=I love this product
```

Response:
```json
{
  "text": "I love this product",
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.9997
    }
  ]
}
```

## Results
- Accuracy: 91.3% on SST-2 benchmark
- Average response time: ~200ms
- Tested with 10+ example inputs

---

## Türkçe Açıklama

FastAPI ve HuggingFace Transformers kullanılarak geliştirilmiş, production'a hazır bir duygu analizi API'si.

## Ne Yapar?
İngilizce metni analiz eder ve metnin duygusunun POZİTİF mi NEGATİF mi olduğunu 0 ile 1 arasında bir güven skoru ile döndürür.

## Teknoloji Yığını
- **FastAPI** — API geliştirmek için yüksek performanslı Python web framework'ü
- **HuggingFace Transformers** — SST-2 veri seti üzerinde ince ayar yapılmış DistilBERT modeli
- **Prometheus** — Metrik toplama ve izleme
- **Grafana** — Metriklerin görselleştirilmesi ve dashboard'lar
- **Docker** — Tutarlı dağıtım için konteynerizasyon

## Yerel Kurulum

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoint'leri

| Metot | Endpoint | Açıklama |
|-------|----------|----------|
| GET | / | Sağlık kontrolü |
| POST | /predict | Duygu analizi yap |
| GET | /metrics | Prometheus metrikleri |

## Örnek Kullanım

İstek:
```
POST /predict?text=I love this product
```

Yanıt:
```json
{
  "text": "I love this product",
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.9997
    }
  ]
}
```
