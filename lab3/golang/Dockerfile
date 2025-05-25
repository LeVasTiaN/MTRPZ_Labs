FROM golang:1.22 AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download && go mod verify

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o fizzbuzz .

FROM gcr.io/distroless/base

WORKDIR /app

COPY --from=builder /app/fizzbuzz .

COPY --from=builder /app/templates/ ./templates/

EXPOSE 8080

CMD ["./fizzbuzz", "serve"]
