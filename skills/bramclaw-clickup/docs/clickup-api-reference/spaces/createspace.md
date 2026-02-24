# Create Space

Add a new Space to a Workspace.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_id}/space": {
      "post": {
        "summary": "Create Space",
        "tags": [
          "Spaces"
        ],
        "description": "Add a new Space to a Workspace.",
        "operationId": "CreateSpace",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateSpacerequest",
                "required": [
                  "name",
                  "multiple_assignees",
                  "features"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "multiple_assignees": {
                    "type": "boolean"
                  },
                  "features": {
                    "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features"
                  }
                },
                "examples": [
                  {
                    "name": "New Space Name",
                    "multiple_assignees": true,
                    "features": {
                      "due_dates": {
                        "enabled": true,
                        "start_date": false,
                        "remap_due_dates": true,
                        "remap_closed_due_date": false
                      },
                      "time_tracking": {
                        "enabled": false
                      },
                      "tags": {
                        "enabled": true
                      },
                      "time_estimates": {
                        "enabled": true
                      },
                      "checklists": {
                        "enabled": true
                      },
                      "custom_fields": {
                        "enabled": true
                      },
                      "remap_dependencies": {
                        "enabled": true
                      },
                      "dependency_warning": {
                        "enabled": true
                      },
                      "portfolios": {
                        "enabled": true
                      }
                    }
                  }
                ]
              },
              "example": {
                "name": "New Space Name",
                "multiple_assignees": true,
                "features": {
                  "due_dates": {
                    "enabled": true,
                    "start_date": false,
                    "remap_due_dates": true,
                    "remap_closed_due_date": false
                  },
                  "time_tracking": {
                    "enabled": false
                  },
                  "tags": {
                    "enabled": true
                  },
                  "time_estimates": {
                    "enabled": true
                  },
                  "checklists": {
                    "enabled": true
                  },
                  "custom_fields": {
                    "enabled": true
                  },
                  "remap_dependencies": {
                    "enabled": true
                  },
                  "dependency_warning": {
                    "enabled": true
                  },
                  "portfolios": {
                    "enabled": true
                  }
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "CreateSpaceresponse",
                  "required": [
                    "id",
                    "name",
                    "private",
                    "statuses",
                    "multiple_assignees",
                    "features",
                    "archived"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "private": {
                      "type": "boolean"
                    },
                    "statuses": {
                      "type": "array",
                      "items": {
                        "title": "Status15",
                        "required": [
                          "id",
                          "status",
                          "type",
                          "orderindex",
                          "color"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "status": {
                            "type": "string"
                          },
                          "type": {
                            "type": "string"
                          },
                          "orderindex": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "color": {
                            "type": "string"
                          }
                        },
                        "examples": [
                          {
                            "id": "p16911531_p8y2WNC6",
                            "status": "to do",
                            "type": "open",
                            "orderindex": 0,
                            "color": "#d3d3d3"
                          }
                        ]
                      },
                      "description": ""
                    },
                    "multiple_assignees": {
                      "type": "boolean"
                    },
                    "features": {
                      "title": "Features1",
                      "required": [
                        "due_dates",
                        "sprints",
                        "points",
                        "custom_items",
                        "tags",
                        "time_estimates",
                        "checklists",
                        "zoom",
                        "milestones",
                        "custom_fields",
                        "remap_dependencies",
                        "dependency_warning",
                        "multiple_assignees",
                        "portfolios",
                        "emails"
                      ],
                      "type": "object",
                      "properties": {
                        "due_dates": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/due_dates"
                        },
                        "sprints": {
                          "title": "Sprints",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": false
                            }
                          ]
                        },
                        "points": {
                          "title": "Points",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": false
                            }
                          ]
                        },
                        "custom_items": {
                          "title": "CustomItems",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": false
                            }
                          ]
                        },
                        "tags": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/tags"
                        },
                        "time_estimates": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/time_estimates"
                        },
                        "checklists": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/checklists"
                        },
                        "zoom": {
                          "title": "Zoom",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": false
                            }
                          ]
                        },
                        "milestones": {
                          "title": "Milestones",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": false
                            }
                          ]
                        },
                        "custom_fields": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/custom_fields"
                        },
                        "remap_dependencies": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/remap_dependencies"
                        },
                        "dependency_warning": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/dependency_warning"
                        },
                        "multiple_assignees": {
                          "title": "MultipleAssignees",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": true
                            }
                          ]
                        },
                        "portfolios": {
                          "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features/properties/portfolios"
                        },
                        "emails": {
                          "title": "Emails",
                          "required": [
                            "enabled"
                          ],
                          "type": "object",
                          "properties": {
                            "enabled": {
                              "type": "boolean"
                            }
                          },
                          "examples": [
                            {
                              "enabled": true
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "due_dates": {
                            "enabled": true,
                            "start_date": false,
                            "remap_due_dates": true,
                            "remap_closed_due_date": false
                          },
                          "sprints": {
                            "enabled": false
                          },
                          "points": {
                            "enabled": false
                          },
                          "custom_items": {
                            "enabled": false
                          },
                          "tags": {
                            "enabled": true
                          },
                          "time_estimates": {
                            "enabled": true
                          },
                          "checklists": {
                            "enabled": true
                          },
                          "zoom": {
                            "enabled": false
                          },
                          "milestones": {
                            "enabled": false
                          },
                          "custom_fields": {
                            "enabled": true
                          },
                          "remap_dependencies": {
                            "enabled": true
                          },
                          "dependency_warning": {
                            "enabled": true
                          },
                          "multiple_assignees": {
                            "enabled": true
                          },
                          "portfolios": {
                            "enabled": true
                          },
                          "emails": {
                            "enabled": true
                          }
                        }
                      ]
                    },
                    "archived": {
                      "type": "boolean"
                    }
                  },
                  "examples": [
                    {
                      "id": "790",
                      "name": "New Space Name",
                      "private": false,
                      "statuses": [
                        {
                          "id": "p16911531_p8y2WNC6",
                          "status": "to do",
                          "type": "open",
                          "orderindex": 0,
                          "color": "#d3d3d3"
                        },
                        {
                          "id": "p17911545_ABo7jSsf",
                          "status": "complete",
                          "type": "closed",
                          "orderindex": 1,
                          "color": "#6bc950"
                        }
                      ],
                      "multiple_assignees": true,
                      "features": {
                        "due_dates": {
                          "enabled": true,
                          "start_date": false,
                          "remap_due_dates": true,
                          "remap_closed_due_date": false
                        },
                        "sprints": {
                          "enabled": false
                        },
                        "points": {
                          "enabled": false
                        },
                        "custom_items": {
                          "enabled": false
                        },
                        "tags": {
                          "enabled": true
                        },
                        "time_estimates": {
                          "enabled": true
                        },
                        "checklists": {
                          "enabled": true
                        },
                        "zoom": {
                          "enabled": false
                        },
                        "milestones": {
                          "enabled": false
                        },
                        "custom_fields": {
                          "enabled": true
                        },
                        "remap_dependencies": {
                          "enabled": true
                        },
                        "dependency_warning": {
                          "enabled": true
                        },
                        "multiple_assignees": {
                          "enabled": true
                        },
                        "portfolios": {
                          "enabled": true
                        },
                        "emails": {
                          "enabled": true
                        }
                      },
                      "archived": false
                    }
                  ]
                },
                "example": {
                  "id": "790",
                  "name": "New Space Name",
                  "private": false,
                  "statuses": [
                    {
                      "id": "p16911531_p8y2WNC6",
                      "status": "to do",
                      "type": "open",
                      "orderindex": 0,
                      "color": "#d3d3d3"
                    },
                    {
                      "id": "p17911545_ABo7jSsf",
                      "status": "complete",
                      "type": "closed",
                      "orderindex": 1,
                      "color": "#6bc950"
                    }
                  ],
                  "multiple_assignees": true,
                  "features": {
                    "due_dates": {
                      "enabled": true,
                      "start_date": false,
                      "remap_due_dates": true,
                      "remap_closed_due_date": false
                    },
                    "sprints": {
                      "enabled": false
                    },
                    "points": {
                      "enabled": false
                    },
                    "custom_items": {
                      "enabled": false
                    },
                    "tags": {
                      "enabled": true
                    },
                    "time_estimates": {
                      "enabled": true
                    },
                    "checklists": {
                      "enabled": true
                    },
                    "zoom": {
                      "enabled": false
                    },
                    "milestones": {
                      "enabled": false
                    },
                    "custom_fields": {
                      "enabled": true
                    },
                    "remap_dependencies": {
                      "enabled": true
                    },
                    "dependency_warning": {
                      "enabled": true
                    },
                    "multiple_assignees": {
                      "enabled": true
                    },
                    "portfolios": {
                      "enabled": true
                    },
                    "emails": {
                      "enabled": true
                    }
                  },
                  "archived": false
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Spaces"
    }
  ]
}
```